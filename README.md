# kickdrops 🎁

[![License: MIT](https://shields.io)](https://opensource.org)
[![Python](https://shields.io)](https://python.org)

Автоматическое получение дропов на платформе Kick прямо в консоли, без необходимости открывать браузер.

Automatic Kick stream drops claimer running entirely in your console. No browser windows required.

---

## 🇷🇺 Инструкция (Russian)

### Основные возможности
* **Работа в консоли:** Минимальное потребление ресурсов, не требует запущенного браузера.
* **Автоматизация:** Скрипт сам отслеживает доступные трансляции и прогресс получения наград.
* **Локализация:** Поддержка нескольких языков интерфейса (`locales`).
* **Гибкая настройка:** Конфигурация через удобный `.ini` файл.

### Системные требования
* Python версии **3.10 или выше**.

### Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd kickdrops
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройка конфигурации:**
   * Переименуйте файл `example_config.ini` в `config.ini`.
   * Откройте `config.ini` и заполните необходимые параметры.
   * Скопируйте свои куки авторизации Kick в файл `cookies.txt`.

4. **Запуск скрипта:**
   * **Linux/macOS:** `bash run.sh` или `python index.py`
   * **Windows:** `python index.py`

---

## 🇺🇸 Instruction (English)

### Features
* **Console-based:** Ultra-low resource usage, functions perfectly without opening a web browser.
* **Automation:** Automatically tracks active streams and monitors your drop progress.
* **Localization:** Multi-language interface support via `locales`.
* **Configurable:** Easy setup using a standard `.ini` configuration file.

### Prerequisites
* Python **3.10 or higher**.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd kickdrops
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   * Rename `example_config.ini` to `config.ini`.
   * Open `config.ini` and specify your preferred settings.
   * Save your logged-in Kick session cookies into `cookies.txt`.

4. **Run the tool:**
   * **Linux/macOS:** `bash run.sh` or `python index.py`
   * **Windows:** `python index.py`

---

## 📄 License / Лицензия

Этот проект распространяется под лицензией **MIT**. Подробности смотрите в файле [LICENSE](LICENSE).

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
