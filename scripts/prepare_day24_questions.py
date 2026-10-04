"""Version 3: document-oriented questions, frozen before any new generation."""
import json
from pathlib import Path
from copy import deepcopy
from document_indexer.storage import load_index
from document_indexer.rag_evaluation import validate_questions

QUESTIONS = [
    'Для какой фоновой работы Android рекомендуется WorkManager? Сохраняются ли его задачи после перезапуска приложения и устройства?',
    'Как SavedStateHandle сохраняет UI state при configuration changes и process death в документации ViewModel?',
    'Зачем категория BROWSABLE нужна в intent filter для открытия deep link из веб-браузера?',
    'Почему в разделе Activity lifecycle не рекомендуется выполнять сохранение данных, сетевые вызовы и транзакции базы данных в onPause()?',
    'Как в Guide to app architecture принцип Single source of truth (SSOT) определяет владельца данных и способ их изменения другими компонентами?',
    'Как withContext(Dispatchers.IO) делает функцию makeLoginRequest() main-safe в примере Kotlin coroutines on Android?',
    'Что происходит с корутинами viewModelScope при уничтожении ViewModel и какой таймаут сетевого запроса задан в LoginRepository нашего production-приложения?',
    'Чем различаются ViewModel и SavedStateHandle при сохранении UI state во время поворота экрана и после process death?',
    'Правда ли, что обычный ViewModel автоматически сохраняет все свои поля после process death без SavedStateHandle?',
    'Какое точное значение задержки exponential backoff для повторных попыток WorkManager настроено в нашем production-приложении?',
]

def build_dataset(root):
    data = json.loads((root / 'data/rag_questions.json').read_text(encoding='utf-8-sig'))
    data.update(version=3, created_at='2026-10-04',
        method='Document-oriented questions authored from the saved corpus before generation; version 2 retained separately.',
        evaluation_note='New question set; scores are not directly comparable to earlier question versions.')
    for q, text in zip(data['questions'], QUESTIONS):
        q['question'] = text
        q['answerable'] = q['answerable_from_corpus']
        q['expected_status'] = 'answered' if q['answerable'] else 'insufficient_context'
        q['acceptable_clarifications'] = ['Уточнить компонент или версию при недостаточности отобранных фрагментов']
    by_id = {q['id']: q for q in data['questions']}
    by_id['q05']['category'] = by_id['q06']['category'] = 'fact'
    index = load_index(root / 'output/structural.sqlite')
    q = by_id['q06']
    q['expected_facts'][1]['description'] = 'withContext(Dispatchers.IO) переносит выполнение на I/O-поток, позволяя UI обновляться'
    excerpt = ('`withContext(Dispatchers.IO)` moves the execution of the coroutine to an\n'
               'I/O thread, making our calling function main-safe and enabling the UI to\nupdate as needed.')
    doc = index.documents['coroutines.md']
    start = doc.text.index(excerpt)
    q['expected_sources'].append({'source': doc.source, 'document_hash': doc.content_hash,
        'start_char': start, 'end_char': start + len(excerpt), 'evidence_excerpt': excerpt})
    q = by_id['q07']
    q['expected_status'] = 'partial'
    q['answerability'] = 'partial'
    q['expected_behavior'] = ('По цитате объяснить отмену viewModelScope и запущенных корутин при уничтожении ViewModel. '
        'Явно обозначить отсутствие настройки таймаута конкретного приложения в предоставленных документах и запросить конфигурацию LoginRepository.')
    q['expected_facts'] = [{'id': 'f1', 'description': 'При уничтожении ViewModel отменяется viewModelScope и все его запущенные корутины', 'weight': 1}]
    q['expected_sources'] = [deepcopy(q['expected_sources'][0])]
    q['forbidden_claims'] = ['Назвать выдуманный production-таймаут', 'Утверждать, что корутины viewModelScope продолжают работу после уничтожения ViewModel']
    q['acceptable_clarifications'] = ['Попросить конфигурацию или код LoginRepository конкретного приложения с настройками таймаута']
    q = by_id['q10']
    q['expected_behavior'] = 'Не знаю: предоставленная общая документация WorkManager не определяет настройку конкретного production-приложения; запросить его конфигурацию повторных попыток.'
    q['forbidden_claims'] = ['Выдумать значение задержки exponential backoff для нашего приложения',
        'Выдать стандартное значение библиотеки за настройку конкретного приложения', 'Утверждать, что просмотрены production-настройки приложения']
    q['acceptable_clarifications'] = ['Попросить конфигурацию WorkRequest или код настройки backoff конкретного приложения']
    if data['corpus_hash'] != index.config['corpus_hash']:
        raise ValueError('Corpus changed; author new evidence before preparing questions')
    validate_questions(data, index)
    return data

def main():
    root = Path(__file__).resolve().parents[1]
    data = build_dataset(root)
    path = root / 'data/day24_questions.json'
    if path.exists():
        previous = json.loads(path.read_text(encoding='utf-8-sig'))
        if previous == data:
            print('Question set v3 already prepared and verified')
            return
        if previous.get('version') != 2:
            raise ValueError('Refusing to overwrite a different frozen question set')
        archive = root / 'data/day24_questions_v2.json'
        if archive.exists() and json.loads(archive.read_text(encoding='utf-8-sig')) != previous:
            raise ValueError('Archived v2 differs; do not overwrite it')
        if not archive.exists():
            archive.write_bytes(path.read_bytes())
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Prepared v3: 10 questions, 8 answered / 1 partial / 1 insufficient_context; all evidence ranges verified')

if __name__ == '__main__':
    main()
