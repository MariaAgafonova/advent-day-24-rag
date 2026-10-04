# День 24 — реальные результаты

Основной run_id: `6c0abd85-45e6-43b7-ad7f-083274e2a9d3`; дата: 2026-10-04T19:32:33.479639+00:00; статус: completed.
Проверено автоматически: 10 результатов / 10 вопросов. Режимы: day24. Ручных оценок: 0 / 10.
День 24: 4 содержательных ответа, 5 / 5 точных валидных цитат; 7 claims, 0 / 7 оценено вручную.
Неоценённая подтверждённость claims и правильность отказов — N/A, а не 0%.

## Условия проверки
Только режим Дня 24. Сравнение с Днём 23 не выполнялось.
Модель: `deepseek-flash`; параметры генерации: `{"temperature": 0.2, "max_output_tokens": 1024, "top_k": 5, "max_context_tokens": 3000, "context_window_tokens": 8192}`.
Поиск и фильтрация: `{"mode": "filter", "retrieval_k": 15, "final_k": 5, "filter_method": "similarity_threshold", "similarity_threshold": 0.85, "calibration_id": null, "reranker_model": null, "reranker_revision": null, "reranker_threshold": null, "reranker_max_length": 512, "rewrite_enabled": false, "calibration_status": "uncalibrated"}`.
Порог и происхождение: `{"value": 0.85, "score_type": "cosine_similarity", "model_id": "intfloat/multilingual-e5-small", "revision": "614241f622f53c4eeff9890bdc4f31cfecc418b3", "index_build_id": "a7f462e7-9aa7-4795-9d5d-b7106c3d43ff", "corpus_hash": "d49278fe920127948b4d5207990dec7f26a7f2230c74c0aa5b7f6984b32bc34d", "calibration_id": null, "origin": "day23_manual_threshold", "calibrated": false}`.
Рубрика зафиксирована до запуска; хеш корпуса и диапазоны источников проверены.
Учёт времени: Each Day 24 answer includes its own preparation and generation time.

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
| mean_latency_ms | 74405.63800011296 | 10 | 7440.5638 |
| usage_coverage | 5 | 5 | 1.0000 |
| mean_generation_tokens | 7009 | 5 | 1401.8000 |
Usage генераций: `{"prompt_tokens": 5901, "completion_tokens": 1108, "total_tokens": 7009}`; вызовов: 5

## Проверки
Полный набор: **158 passed, 3 deselected** (`python -m pytest -q`).
Три integration-теста прежних дней исключены стандартным маркером. Реальные embedding-поиск и LLM проверены запуском выше.
Unit-тесты проверяют схему, ссылки, точные и выдуманные/обрезанные цитаты, отказ без генерации, partial, единственное исправление, технические ошибки, N/A и сохранение ручной оценки.
Streamlit AppTest проверяет экран, открытие источника с подсветкой и историю без LLM. Сохранены тесты прежних режимов.
Индекс не перестраивался. SHA-256 файлов:
- `structural.sqlite`: `9dd3c7b9cbe91c32eff9313cd841e8b0da03dd35f77fddb361bc208e39c45614`
- `fixed.sqlite`: `581195a4108444f73b69362c0b524eef2a0612b2135f7b0ece9e09a3e5408dc1`

## Экспорт и ручная проверка
- [JSON — полный сохранённый отчёт](output/day24_experiments/exports/6c0abd85-45e6-43b7-ad7f-083274e2a9d3-cd773b70/report.json)
- [CSV — полный сохранённый отчёт](output/day24_experiments/exports/6c0abd85-45e6-43b7-ad7f-083274e2a9d3-cd773b70/report.csv)
- [MD — полный сохранённый отчёт](output/day24_experiments/exports/6c0abd85-45e6-43b7-ad7f-083274e2a9d3-cd773b70/report.md)

Откройте «Проверяемые цитаты» → «10 контрольных вопросов» или «История», выберите основной run_id и заполните ручные оценки каждого ответа.
В UI раздельно проверяются смысл каждой цитаты/claim, новые факты в answer, условия, корректность, полнота и отказы. После сохранения метрики обновляются без LLM.

## Ограничения
Наличие точной цитаты не доказывает смысловую поддержку. Нет гарантии отсутствия ошибок. Смысл оценивается человеком.
Наблюдаются отказы на вопросах, для которых в полном корпусе зафиксированы доказательства. Порог и усечение контекста могут терять нужную информацию; это не означает отсутствие ответа во всей базе. Порог по тестовым ответам не подстраивался.
Ранее выполненные парные эксперименты сохранены в истории и не входят в текущую проверку.
Пустые источники/цитаты отказа — N/A. Неоценённая семантика исключена из средних.