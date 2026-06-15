```markdown
# KickAutoDrops Enhanced

[RU](README.ru.md) [EN](README.md)

> **Based on** [KickAutoDrops](https://github.com/PBA4EVSKY/kickautodrops) by [@PBA4EVSKY](https://github.com/PBA4EVSKY).  
> This enhanced version focuses on **Linux-first compatibility**, **automated setup**, and **improved user experience**.

---

**KickAutoDrops Enhanced** — это минималистичный инструмент автоматизации, предназначенный для эффективного сбора игровых дропов **Rust** с сайта [Kick.com](https://kick.com), **без необходимости реально смотреть трансляции**.  
Приложение работает в фоновом режиме, имитируя просмотр стримов через взаимодействие с API Kick.com. Это позволяет получать дропы, экономя трафик и системные ресурсы.

---

## ⚙️ Как это работает

Каждые **10 секунд** приложение имитирует просмотр стрима, запрашивая метаданные и отправляя необходимые запросы на Kick.com.  
Этого достаточно для продвижения таймеров дропов, **без загрузки видео или аудио данных**.

Для поддержания актуального статуса канала (ONLINE / OFFLINE), приложение устанавливает **WebSocket-соединение**, через которое получает события в реальном времени:
- Запуск и завершение стримов  
- Изменения игр или категорий  
- Обновления прогресса дропов  
- Изменения количества зрителей  

---

## 🧩 Установка

### Вариант 1: Готовая сборка (скоро)

> *Сборки для Linux (и других ОС) будут доступны в разделе [Releases](https://github.com/InCoGnItO-228/kickdrops-enhanced/releases) после первого релиза.*

### Вариант 2: Запуск из исходников (рекомендуется для Linux)

1. Установите расширение для экспорта cookies:
   - [Get cookies.txt LOCALLY (Chrome)](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - [Get cookies.txt LOCALLY (Firefox)](https://addons.mozilla.org/en-US/firefox/addon/get-cookies-txt-locally/)  
2. Зайдите на [kick.com](https://kick.com), авторизуйтесь  
3. Экспортируйте cookies и сохраните их в файл **`cookies.txt`** в корне проекта  
4. Запустите один раз — всё настроится автоматически:

```bash
git clone https://github.com/InCoGnItO-228/kickdrops-enhanced.git
cd kickdrops-enhanced
./run.sh
```

Скрипт `run.sh`:
- создаст виртуальное окружение (`.venv`)  
- установит все зависимости (`curl_cffi`, `websockets`)  
- проверит наличие `cookies.txt`  
- запустит приложение

> **Требования**: Python 3.10+, Google Chrome (для экспорта кук через расширение), `libcurl` (обычно уже есть в системе)

---

### Вариант 3: Ручная сборка (опционально)

```bash
git clone https://github.com/InCoGnItO-228/kickdrops-enhanced.git
cd kickdrops-enhanced

python -m venv .venv
source .venv/bin/activate

pip install curl_cffi websockets pyinstaller
pyinstaller index.spec  # исполняемый файл появится в папке dist/
```

---

## ❤️ Благодарности и вклад

Исходная идея и базовая реализация принадлежат **[@PBA4EVSKY](https://github.com/PBA4EVSKY)**.  
Этот проект — улучшенная, Linux-ориентированная версия, созданная для удобства и стабильности.

Хотите улучшить этот проект?  
Смело **форкайте репозиторий** и отправляйте **pull request** — все вкладчики приветствуются и ценятся ❤️

---

## 📂 Структура проекта

- `index.py` — основной скрипт  
- `run.sh` — автоматический запускатор для Linux  
- `cookies.txt` — файл с экспортированными cookies (не коммитится)  
- `config.ini` — настройки (генерируется автоматически)  
- `.venv/` — виртуальное окружение (не коммитится)
```
