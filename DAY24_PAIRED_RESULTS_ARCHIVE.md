# День 24 — реальные результаты

Основной run_id: `c713696d-02e6-4b12-86ae-77db32ef8c89`; дата: 2026-10-02T20:49:13.381374+00:00; статус: completed.
Проверено автоматически: 20 результатов / 10 вопросов × 2 режима. Ручных оценок: 0 / 20.
День 24: 4 содержательных ответа, 5 / 5 точных валидных цитат; 7 claims, 0 / 7 оценено вручную.
Подтверждённость claims — N/A (0 оценённых), а не 0%. Правильные и ложные отказы — N/A до ручной проверки.

## Условия сравнения
Одинаковые вопросы, сохранённый structural-индекс, фактический контекст, deepseek-flash, temperature=0.2, max_output_tokens=1024, max_context_tokens=3000, context_window_tokens=8192.
Rewrite выключен. Cosine ≥ 0.85, retrieval_k=15, final_k=5. Порог унаследован, не откалиброван. Старый prompt Дня 23 сохранён.
E5: intfloat/multilingual-e5-small, revision 614241f622f53c4eeff9890bdc4f31cfecc418b3.
Версия prompt Дня 24: day24-evidence-v2. Рубрика зафиксирована до первого запуска; хеш и диапазоны проверены.
Время учитывает общую подготовку и холодную загрузку модели для обеих веток; генерация измеряется отдельно. Запуски используют общую подготовку, их время нельзя складывать как независимую wall-clock длительность.

## Ответы Дня 24
| Вопрос | Статус | Причина | Цитаты | Claims | Генерации |
|---|---|---|---:|---:|---:|
| q01 | insufficient_context | below_relevance_threshold | 0 | 0 | 0 |
| q02 | answered | — | 1 | 2 | 1 |
| q03 | answered | — | 1 | 2 | 1 |
| q04 | insufficient_context | below_relevance_threshold | 0 | 0 | 0 |
| q05 | insufficient_context | below_relevance_threshold | 0 | 0 | 0 |
| q06 | insufficient_context | below_relevance_threshold | 0 | 0 | 0 |
| q07 | insufficient_context | insufficient_evidence | 0 | 0 | 1 |
| q08 | answered | — | 2 | 2 | 1 |
| q09 | answered | — | 1 | 1 | 1 |
| q10 | insufficient_context | below_relevance_threshold | 0 | 0 | 0 |

## Метрики и знаменатели
### day23
| Метрика | Числитель | Знаменатель | Значение |
|---|---:|---:|---:|
| review_coverage | 0 | 10 | 0.0000 |
| classified_answers | 0 | 10 | 0.0000 |
| with_sources | 0 | 0 | N/A |
| with_exact_quotes | 0 | 0 | N/A |
| valid_quotes | 0 | 0 | N/A |
| valid_quotes_all_attempts | 0 | 0 | N/A |
| supported_claims | 0 | 0 | N/A |
| correctness | 0 | 0 | N/A |
| completeness | 0 | 0 | N/A |
| correct_refusals | 0 | 0 | N/A |
| false_refusals_corpus | 0 | 0 | N/A |
| false_refusals_context | 0 | 0 | N/A |
| refusals_with_clarification | 0 | 0 | N/A |
| initial_validation_errors | 0 | 0 | N/A |
| final_validation_failures | 0 | 10 | 0.0000 |
| technical_errors | 0 | 10 | 0.0000 |
| repair_calls | 0 | 10 | 0.0000 |
| mean_latency_ms | 79619.61259989766 | 10 | 7961.9613 |
| usage_coverage | 5 | 5 | 1.0000 |
| mean_generation_tokens | 4050 | 5 | 810.0000 |
Usage генераций: `{"prompt_tokens": 3501, "completion_tokens": 549, "total_tokens": 4050}`; вызовов: 5
### day24
| Метрика | Числитель | Знаменатель | Значение |
|---|---:|---:|---:|
| review_coverage | 0 | 10 | 0.0000 |
| classified_answers | 10 | 10 | 1.0000 |
| with_sources | 4 | 4 | 1.0000 |
| with_exact_quotes | 4 | 4 | 1.0000 |
| valid_quotes | 5 | 5 | 1.0000 |
| valid_quotes_all_attempts | 5 | 5 | 1.0000 |
| supported_claims | 0 | 0 | N/A |
| correctness | 0 | 0 | N/A |
| completeness | 0 | 0 | N/A |
| correct_refusals | 0 | 0 | N/A |
| false_refusals_corpus | 0 | 0 | N/A |
| false_refusals_context | 0 | 0 | N/A |
| refusals_with_clarification | 6 | 6 | 1.0000 |
| initial_validation_errors | 0 | 5 | 0.0000 |
| final_validation_failures | 0 | 10 | 0.0000 |
| technical_errors | 0 | 10 | 0.0000 |
| repair_calls | 0 | 10 | 0.0000 |
| mean_latency_ms | 80959.8215999431 | 10 | 8095.9822 |
| usage_coverage | 5 | 5 | 1.0000 |
| mean_generation_tokens | 7029 | 5 | 1405.8000 |
Usage генераций: `{"prompt_tokens": 5901, "completion_tokens": 1128, "total_tokens": 7029}`; вызовов: 5

## Проверки
Полный набор: **158 passed, 3 deselected** (`python -m pytest -q`).
Три integration-теста прежних дней исключены стандартным маркером. Реальные embedding-поиск и LLM проверены парным запуском выше.
Unit-тесты проверяют схему, ссылки, точные и выдуманные/обрезанные цитаты, отказ без генерации, partial, единственное исправление, технические ошибки, N/A и сохранение ручной оценки.
Streamlit AppTest проверяет экран, открытие источника с подсветкой и историю без LLM. Сохранены тесты прежних режимов.
Индекс не перестраивался. SHA-256 файлов:
- `structural.sqlite`: `642c8aa8f83f19d38685764afc5a21c9ab3788ac9bc885e19c6b1361bd075914`
- `fixed.sqlite`: `ef698bfe6ad7f4fabae7310c265ef084a33b395a54afa2d146fb612da699495f`

## Экспорт и ручная проверка
- [JSON — полный сохранённый отчёт](output/day24_experiments/exports/c713696d-02e6-4b12-86ae-77db32ef8c89-92a4c45b/report.json)
- [CSV — полный сохранённый отчёт](output/day24_experiments/exports/c713696d-02e6-4b12-86ae-77db32ef8c89-92a4c45b/report.csv)
- [MD — полный сохранённый отчёт](output/day24_experiments/exports/c713696d-02e6-4b12-86ae-77db32ef8c89-92a4c45b/report.md)

Откройте «Проверяемые цитаты» → «10 контрольных вопросов» или «История», выберите основной run_id и заполните ручные оценки каждого ответа.
В UI раздельно проверяются смысл каждой цитаты/claim, новые факты в answer, условия, корректность, полнота и отказы. После сохранения метрики обновляются без LLM.

## Ограничения и предварительный запуск
Наличие точной цитаты не доказывает смысловую поддержку. Нет гарантии отсутствия ошибок. До человеческой оценки выводы о превосходстве режима не делаются.
Наблюдаются отказы на вопросах, для которых в полном корпусе зафиксированы доказательства. Порог и усечение контекста могут терять нужную информацию; это не означает отсутствие ответа во всей базе. Порог по тестовым ответам не подстраивался.
Предварительный run e7e9af8f-7436-4256-92cc-bdb987799c23 сохранён отдельно. Он выявил риск фактического пересказа в отказе с пустыми claims. В v2 отображается безопасный текст отказа, исходный вывод остаётся в трассировке. Также в итоговом запуске учтено время холодной подготовки. Для сравнения использовать основной run выше.
Пустые источники/цитаты отказа — N/A. Неоценённая семантика исключена из средних. Для старого режима новая JSON-схема не является критерием правильности.