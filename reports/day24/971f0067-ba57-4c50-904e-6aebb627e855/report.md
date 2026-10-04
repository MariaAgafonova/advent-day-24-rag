# День 24: проверка контрольных вопросов

Run: 971f0067-ba57-4c50-904e-6aebb627e855
Точность цитат не доказывает смысловую поддержку. Неоценённая семантика — N/A.
Порог и происхождение: `{"value": 0.85, "score_type": "cosine_similarity", "model_id": "intfloat/multilingual-e5-small", "revision": "614241f622f53c4eeff9890bdc4f31cfecc418b3", "index_build_id": "313b9408-c32e-481e-bc50-74941e11de32", "corpus_hash": "d49278fe920127948b4d5207990dec7f26a7f2230c74c0aa5b7f6984b32bc34d", "calibration_id": null, "origin": "day23_manual_threshold", "calibrated": false}`
Проверяется только режим Дня 24. Время включает подготовку и генерацию каждого ответа.

## day24
| Метрика | Числитель | Знаменатель | Значение |
|---|---:|---:|---:|
| review_coverage | 0 | 10 | 0.0000 |
| classified_answers | 10 | 10 | 1.0000 |
| with_sources | 9 | 9 | 1.0000 |
| with_exact_quotes | 9 | 9 | 1.0000 |
| valid_quotes | 18 | 18 | 1.0000 |
| valid_quotes_all_attempts | 18 | 18 | 1.0000 |
| supported_claims | 0 | 0 | N/A |
| correctness | 0 | 0 | N/A |
| completeness | 0 | 0 | N/A |
| correct_refusals | 0 | 0 | N/A |
| false_refusals_corpus | 0 | 0 | N/A |
| false_refusals_context | 0 | 0 | N/A |
| refusals_with_clarification | 1 | 1 | 1.0000 |
| initial_validation_errors | 0 | 9 | 0.0000 |
| final_validation_failures | 0 | 10 | 0.0000 |
| technical_errors | 0 | 10 | 0.0000 |
| repair_calls | 0 | 10 | 0.0000 |
| mean_latency_ms | 83048.94320003223 | 10 | 8304.8943 |
| usage_coverage | 9 | 9 | 1.0000 |
| mean_generation_tokens | 13444 | 9 | 1493.7778 |

## q01 · day24
Для какой фоновой работы Android рекомендуется WorkManager? Сохраняются ли его задачи после перезапуска приложения и устройства?
Статус: answered; причина: —
WorkManager предназначен для работы, которая должна надёжно выполняться, даже если пользователь уходит с экрана, приложение завершается или устройство перезагружается. Примеры: отправка логов или аналитики в бэкенд-сервисы и периодическая синхронизация данных приложения с сервером. Он не предназначен для внутрипроцессной фоновой работы, которую можно безопасно прервать при завершении процесса приложения, и не является общим решением для всей работы, требующей немедленного выполнения.

### Источники
- [S1] workmanager.md · section: [['Task scheduling Stay organized with collections Save and categorize content based on your preferences.', 'Use WorkManager for reliable work']] · chunk_id: 9eba32e6a6d8e331dd077239a27d35a00d4f9d9bec90c8741dcee482ad4b3b93

### Утверждения и доказательства
- C1: WorkManager предназначен для работы, которая должна надёжно выполняться, даже если пользователь уходит с экрана, приложение завершается или устройство перезагружается. [Q1]
- C2: Примеры: отправка логов или аналитики в бэкенд-сервисы и периодическая синхронизация данных приложения с сервером. [Q2]
- C3: WorkManager не предназначен для внутрипроцессной фоновой работы, которую можно безопасно прервать при завершении процесса приложения, и не является общим решением для всей работы, требующей немедленного выполнения. [Q3]

### Цитаты
### Q1 · Task scheduling Stay organized with collections Save and categorize content based on your preferences. · workmanager.md
Раздел: [['Task scheduling Stay organized with collections Save and categorize content based on your preferences.', 'Use WorkManager for reliable work']]; строки 122–135; чанки: ['9eba32e6a6d8e331dd077239a27d35a00d4f9d9bec90c8741dcee482ad4b3b93']
> WorkManager is intended for work that is required to **run reliably** even if
> the user navigates off a screen, the app exits, or the device restarts.
### Q2 · Task scheduling Stay organized with collections Save and categorize content based on your preferences. · workmanager.md
Раздел: [['Task scheduling Stay organized with collections Save and categorize content based on your preferences.', 'Use WorkManager for reliable work']]; строки 122–135; чанки: ['9eba32e6a6d8e331dd077239a27d35a00d4f9d9bec90c8741dcee482ad4b3b93']
> * Sending logs or analytics to backend services.
> * Periodically syncing application data with a server.
### Q3 · Task scheduling Stay organized with collections Save and categorize content based on your preferences. · workmanager.md
Раздел: [['Task scheduling Stay organized with collections Save and categorize content based on your preferences.', 'Use WorkManager for reliable work']]; строки 122–135; чанки: ['9eba32e6a6d8e331dd077239a27d35a00d4f9d9bec90c8741dcee482ad4b3b93']
> WorkManager is not intended for in-process background work that can safely be
> terminated if the app process goes away. It is also not a general solution for
> all work that requires immediate execution.
Ручная оценка: {"status": "unreviewed"}

## q02 · day24
Как SavedStateHandle сохраняет UI state при configuration changes и process death в документации ViewModel?
Статус: answered; причина: —
SavedStateHandle позволяет сохранять данные не только при configuration changes, но и при process death, сохраняя UI state, даже когда пользователь закрывает приложение и открывает его позже.

### Источники
- [S1] viewmodel.md · section: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']] · chunk_id: 90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac

### Утверждения и доказательства
- C1: SavedStateHandle позволяет сохранять данные не только при configuration changes, но и при process death. [CIT1]
- C2: SavedStateHandle позволяет сохранять UI state, даже когда пользователь закрывает приложение и открывает его позже. [CIT2]

### Цитаты
### CIT1 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']]; строки 84–92; чанки: ['90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac']
> [SavedStateHandle](/topic/libraries/architecture/viewmodel/viewmodel-savedstate) lets you persist data not just through configuration
> changes, but across process death.
### CIT2 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']]; строки 84–92; чанки: ['90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac']
> That is, it lets you keep the UI
> state intact even when the user closes the app and opens it at a later time.
Ручная оценка: {"status": "unreviewed"}

## q03 · day24
Зачем категория BROWSABLE нужна в intent filter для открытия deep link из веб-браузера?
Статус: answered; причина: —
Категория BROWSABLE требуется в intent filter, чтобы deep link можно было открыть из веб-браузера.

### Источники
- [S2] deep-links.md · section: [['Create deep links Stay organized with collections Save and categorize content based on your preferences.', 'Add intent filters for incoming links']] · chunk_id: a1740f4d32f6f29e2130c997380b19e02e26d487e1adb9d2e9f190aa8e526203

### Утверждения и доказательства
- C1: Категорию BROWSABLE нужно включить в intent filter. [CIT1]

### Цитаты
### CIT1 · Create deep links Stay organized with collections Save and categorize content based on your preferences. · deep-links.md
Раздел: [['Create deep links Stay organized with collections Save and categorize content based on your preferences.', 'Add intent filters for incoming links']]; строки 95–103; чанки: ['a1740f4d32f6f29e2130c997380b19e02e26d487e1adb9d2e9f190aa8e526203']
> Include the [`BROWSABLE`](/reference/android/content/Intent#CATEGORY_BROWSABLE) category. It is requir
Ручная оценка: {"status": "unreviewed"}

## q04 · day24
Почему в разделе Activity lifecycle не рекомендуется выполнять сохранение данных, сетевые вызовы и транзакции базы данных в onPause()?
Статус: answered; причина: —
В разделе Activity lifecycle указано, что выполнение onPause очень краткое и может не дать достаточно времени для операций сохранения, поэтому такие операции могут не завершиться до окончания метода.

### Источники
- [S1] lifecycle.md · section: [['The activity lifecycle Stay organized with collections Save and categorize content based on your preferences.', 'Lifecycle callbacks', 'onPause']] · chunk_id: 382fd5b5c6bac46b05a4103e313b82a5384714e04ff6e7acceb1ab4f0e9ca72c

### Утверждения и доказательства
- C1: onPause выполняется очень кратко и не обязательно даёт достаточно времени для операций сохранения. [Q1]
- C2: Поэтому не следует использовать onPause для сохранения данных приложения или пользователя, сетевых вызовов или транзакций базы данных. [Q2]
- C3: Такая работа может не завершиться до завершения метода. [Q3]

### Цитаты
### Q1 · The activity lifecycle Stay organized with collections Save and categorize content based on your preferences. · lifecycle.md
Раздел: [['The activity lifecycle Stay organized with collections Save and categorize content based on your preferences.', 'Lifecycle callbacks', 'onPause']]; строки 276–299; чанки: ['382fd5b5c6bac46b05a4103e313b82a5384714e04ff6e7acceb1ab4f0e9ca72c']
> `onPause` execution is very brief and does not necessarily offer enough time to
> perform save operations.
### Q2 · The activity lifecycle Stay organized with collections Save and categorize content based on your preferences. · lifecycle.md
Раздел: [['The activity lifecycle Stay organized with collections Save and categorize content based on your preferences.', 'Lifecycle callbacks', 'onPause']]; строки 276–299; чанки: ['382fd5b5c6bac46b05a4103e313b82a5384714e04ff6e7acceb1ab4f0e9ca72c']
> For this reason, **don't** use `onPause` to save
> application or user data, make network calls, or execute database transactions.
### Q3 · The activity lifecycle Stay organized with collections Save and categorize content based on your preferences. · lifecycle.md
Раздел: [['The activity lifecycle Stay organized with collections Save and categorize content based on your preferences.', 'Lifecycle callbacks', 'onPause']]; строки 276–299; чанки: ['382fd5b5c6bac46b05a4103e313b82a5384714e04ff6e7acceb1ab4f0e9ca72c']
> Such work might not complete before the method completes.
Ручная оценка: {"status": "unreviewed"}

## q05 · day24
Как в Guide to app architecture принцип Single source of truth (SSOT) определяет владельца данных и способ их изменения другими компонентами?
Статус: answered; причина: —
Принцип SSOT назначает единственного владельца для каждого типа данных: только SSOT может изменять или мутировать данные. SSOT предоставляет данные через неизменяемый тип, а для изменения данных предоставляет функции или принимает события, которые могут вызывать другие типы.

### Источники
- [S1] architecture.md · section: [['Guide to app architecture Stay organized with collections Save and categorize content based on your preferences.', 'Common architectural principles', 'Single source of truth']] · chunk_id: 51b51164a956f0285623e84b73f35cab76fec74b54af1a74d75c2a892815fa81

### Утверждения и доказательства
- C1: При определении нового типа данных в приложении ему назначается единственный источник истины (SSOT). [Q1]
- C2: SSOT является владельцем данных, и только SSOT может их изменять или мутировать. [Q2]
- C3: SSOT предоставляет данные через неизменяемый тип, а для изменения данных предоставляет функции или принимает события, которые могут вызывать другие типы. [Q3]

### Цитаты
### Q1 · Guide to app architecture Stay organized with collections Save and categorize content based on your preferences. · architecture.md
Раздел: [['Guide to app architecture Stay organized with collections Save and categorize content based on your preferences.', 'Common architectural principles', 'Single source of truth']]; строки 97–114; чанки: ['51b51164a956f0285623e84b73f35cab76fec74b54af1a74d75c2a892815fa81']
> When a new data type is defined in your app, assign a single source
> of truth (SSOT) to it.
### Q2 · Guide to app architecture Stay organized with collections Save and categorize content based on your preferences. · architecture.md
Раздел: [['Guide to app architecture Stay organized with collections Save and categorize content based on your preferences.', 'Common architectural principles', 'Single source of truth']]; строки 97–114; чанки: ['51b51164a956f0285623e84b73f35cab76fec74b54af1a74d75c2a892815fa81']
> The SSOT is the *owner* of that data, and only the SSOT
> can modify or mutate it.
### Q3 · Guide to app architecture Stay organized with collections Save and categorize content based on your preferences. · architecture.md
Раздел: [['Guide to app architecture Stay organized with collections Save and categorize content based on your preferences.', 'Common architectural principles', 'Single source of truth']]; строки 97–114; чанки: ['51b51164a956f0285623e84b73f35cab76fec74b54af1a74d75c2a892815fa81']
> To achieve this, the SSOT exposes the data using an
> immutable type; to modify the data, the SSOT exposes functions or receives
> events that other types can call.
Ручная оценка: {"status": "unreviewed"}

## q06 · day24
Как withContext(Dispatchers.IO) делает функцию makeLoginRequest() main-safe в примере Kotlin coroutines on Android?
Статус: answered; причина: —
withContext(Dispatchers.IO) перемещает выполнение корутины в поток ввода-вывода (I/O), что делает вызывающую функцию main-safe и позволяет UI обновляться по мере необходимости.

### Источники
- [S1] coroutines.md · section: [['Kotlin coroutines on Android Stay organized with collections Save and categorize content based on your preferences.', 'Use coroutines for main-safety']] · chunk_id: 08a243620ad9654bfa75c0a718bc912bc17f0d3e06e202f485980501b205998f

### Утверждения и доказательства
- C1: withContext(Dispatchers.IO) перемещает выполнение корутины в поток ввода-вывода (I/O). [CIT1]
- C2: Это делает вызывающую функцию main-safe и позволяет UI обновляться по мере необходимости. [CIT2]

### Цитаты
### CIT1 · Kotlin coroutines on Android Stay organized with collections Save and categorize content based on your preferences. · coroutines.md
Раздел: [['Kotlin coroutines on Android Stay organized with collections Save and categorize content based on your preferences.', 'Use coroutines for main-safety']]; строки 186–219; чанки: ['08a243620ad9654bfa75c0a718bc912bc17f0d3e06e202f485980501b205998f']
> `withContext(Dispatchers.IO)` moves the execution of the coroutine to an
> I/O thread
### CIT2 · Kotlin coroutines on Android Stay organized with collections Save and categorize content based on your preferences. · coroutines.md
Раздел: [['Kotlin coroutines on Android Stay organized with collections Save and categorize content based on your preferences.', 'Use coroutines for main-safety']]; строки 186–219; чанки: ['08a243620ad9654bfa75c0a718bc912bc17f0d3e06e202f485980501b205998f']
> making our calling function main-safe and enabling the UI to
> update as needed.
Ручная оценка: {"status": "unreviewed"}

## q07 · day24
Что происходит с корутинами viewModelScope при уничтожении ViewModel и какой таймаут сетевого запроса задан в LoginRepository нашего production-приложения?
Статус: partial; причина: —
В предоставленных фрагментах подтверждается только часть про viewModelScope: при очистке ViewModel владельцем ViewModelStoreOwner в конце его жизненного цикла ViewModel также отменяет CoroutineScope. Таймаут сетевого запроса в LoginRepository production-приложения в доступных фрагментах не указан.

### Источники
- [S1] viewmodel.md · section: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'The lifecycle of a ViewModel', 'Clearing ViewModel dependencies']] · chunk_id: 00e2d52225c30528b39fa8b3c31072a11467ae96d918b5c7e7b9bcd42b4e66af

### Утверждения и доказательства
- C1: Когда ViewModelStoreOwner очищает ViewModel в конце его жизненного цикла, ViewModel также отменяет CoroutineScope. [CIT1]

### Цитаты
### CIT1 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'The lifecycle of a ViewModel', 'Clearing ViewModel dependencies']]; строки 199–207; чанки: ['00e2d52225c30528b39fa8b3c31072a11467ae96d918b5c7e7b9bcd42b4e66af']
> When the
> `ViewModelStoreOwner` clears the ViewModel at the end of its lifecycle, the
> ViewModel also cancels the `CoroutineScope`.
Укажите, пожалуйста, где задан таймаут сетевого запроса в LoginRepository production-приложения (файл/модуль/конфигурация), чтобы я мог найти его значение.
Ручная оценка: {"status": "unreviewed"}

## q08 · day24
Чем различаются ViewModel и SavedStateHandle при сохранении UI state во время поворота экрана и после process death?
Статус: partial; причина: —
В предоставленных фрагментах есть сведения только о SavedStateHandle: он позволяет сохранять данные не только при изменениях конфигурации, но и после process death, то есть сохранять UI state, когда пользователь закрывает приложение и открывает его позже. Прямого сравнения с ViewModel по этому вопросу в доступных фрагментах нет.

### Источники
- [S1] viewmodel.md · section: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']] · chunk_id: 90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac

### Утверждения и доказательства
- C1: SavedStateHandle позволяет сохранять данные не только при изменениях конфигурации, но и после process death. [Q1]
- C2: SavedStateHandle позволяет сохранять UI state, когда пользователь закрывает приложение и открывает его позже. [Q2]

### Цитаты
### Q1 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']]; строки 84–92; чанки: ['90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac']
> [SavedStateHandle](/topic/libraries/architecture/viewmodel/viewmodel-savedstate) lets you persist data not just through configuration
> changes, but across process death.
### Q2 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']]; строки 84–92; чанки: ['90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac']
> That is, it lets you keep the UI
> state intact even when the user closes the app and opens it at a later time.
Нужно ли сравнить ViewModel и SavedStateHandle по другим аспектам, например по области видимости или способу использования в качестве state holder?
Ручная оценка: {"status": "unreviewed"}

## q09 · day24
Правда ли, что обычный ViewModel автоматически сохраняет все свои поля после process death без SavedStateHandle?
Статус: answered; причина: —
Нет. Обычный ViewModel сам по себе не сохраняет поля после process death: для этого нужен SavedStateHandle.

### Источники
- [S1] viewmodel.md · section: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']] · chunk_id: 90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac

### Утверждения и доказательства
- C1: SavedStateHandle позволяет сохранять данные не только при изменениях конфигурации, но и после process death. [Q1]

### Цитаты
### Q1 · ViewModel overview Part of Android Jetpack . · viewmodel.md
Раздел: [['ViewModel overview \xa0\xa0Part of [Android Jetpack](/jetpack).', 'ViewModel benefits', 'Persistence', 'SavedStateHandle']]; строки 84–92; чанки: ['90a7163649a6f4bf618093af5dcf2a6b3c1cdc5cc20a5ab0f756fb2c5de252ac']
> [SavedStateHandle](/topic/libraries/architecture/viewmodel/viewmodel-savedstate) lets you persist data not just through configuration
> changes, but across process death.
Ручная оценка: {"status": "unreviewed"}

## q10 · day24
Какое точное значение задержки exponential backoff для повторных попыток WorkManager настроено в нашем production-приложении?
Статус: insufficient_context; причина: below_relevance_threshold
Не знаю: найденные фрагменты недостаточно релевантны вопросу.

### Источники
Нет источников: подтверждённый ответ не сформирован.

### Утверждения и доказательства

### Цитаты
Нет цитат: доказательства для ответа не представлены.
Уточните тему или название документа, в котором нужно искать ответ.
Ручная оценка: {"status": "unreviewed"}

## Выводы и ограничения
Смысловая оценка выполняется человеком через интерфейс. Пока она не завершена, выводы о корректности, полноте, подтверждённости и правильности отказов не делаются.
Порог 0.85 унаследован из Дня 23 и не откалиброван. 10 вопросов не дают статистической гарантии.
Полная трассировка, исходные выводы, ошибки и обе попытки сохранены в JSON.