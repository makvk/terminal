# VFS Shell Emulator

> Вариант 3
> Простая командная оболочка (shell), работающая поверх **виртуальной файловой системы** (VFS) на основе `.zip`-архива.  
> Поддерживает команды, скрипты и переменные окружения — всё, как в настоящем терминале 💻

---

## ✨ Возможности

Работа с **виртуальной файловой системой** в `.zip`  
Поддержка **интерактивного режима** и **режима выполнения скриптов**  
Обработка **переменных окружения** (`$VAR_NAME`)  
Простое расширение — добавляй свои команды!  
Встроенные команды:

| Команда | Назначение |
|----------|-------------|
| `cd` | переход по виртуальным директориям |
| `ls` | вывод содержимого каталога |
| `echo` | вывод текста |
| `uniq` | вывод уникальных аргументов |
| `whoami` | показывает текущего пользователя |
| `exit` | завершает программу |

---

## 🧱 Структура проекта

    project/
    │
    ├── main.py # Главный исполняемый файл
    │
    ├── command_handlers/ # Обработчики команд
    │ ├── init.py
    │ ├── command.py # Базовый класс Command
    │ ├── cd.py # Команда cd
    │ ├── ls.py # Команда ls
    │ ├── echo.py # Команда echo
    │ ├── uniq.py # Команда uniq
    │ ├── whoami.py # Команда whoami
    │ ├── exit.py # Команда exit
    │
    ├── vfs/
    │ └── disk.zip # Виртуальная файловая система (архив)
    │
    └── scripts/
    ├── test.script # Пример скрипта
    └── test1.script # Ещё один пример


---

## ⚙️ Установка и запуск

### 1️⃣ Требования
- Python **3.8+**
- Только стандартная библиотека (`os`, `sys`, `zipfile`, `getpass`, `abc`)

### 2️⃣ Клонирование проекта
```bash
git clone https://github.com/username/vfs-shell.git
cd vfs-shell
```

## 3️⃣ Запуск в интерактивном режиме

```bash
python3 main.py ./vfs/disk.zip
```

### 📟 Пример:
```bash
disk> ls
📁home 📁bin 📄readme.txt
disk> cd home
disk/home> echo Привет, мир!
Привет, мир!
```

### 📜 Выполнение скриптов
    
    Можно передавать сразу несколько файлов .script:
    
    python3 main.py ./vfs/disk.zip ./scripts/test.script ./scripts/test1.script
    
    Все команды из скриптов будут выполнены автоматически, как будто вы их вводили вручную.
    
    Если в скрипте есть ошибки — они будут показаны после выполнения:
    
    errors in script: unknown_command bad_cmd

### 💡 Переменные окружения

Поддерживается подстановка системных переменных через $VAR_NAME.

```bash
export GREETING="echo Hello World"
python3 main.py ./vfs/disk.zip
disk> $GREETING
Hello World
```

### 🧠 Пример скрипта

#### Файл scripts/test.script:
```bash
echo Начало теста
ls
cd home
ls
whoami
uniq apple apple banana
cd ..
exit
```
#### Вывод:

```bash
Имя скрипта: main.py
Имя VFS: ./vfs/disk.zip
Переданные аргументы: ./scripts/test.script

disk> echo Начало теста
Начало теста
disk> ls
📁home 📁bin 📄readme.txt
disk> cd home
disk/home> ls
📁user
disk/home> whoami
user
disk/home> uniq apple apple banana
apple banana
disk/home> cd ..
disk> exit
```

## 🧩 Архитектура
🔹 Command (базовый класс)

    Определён в command.py

    Загружает список файлов из архива (self.all_members)

    Имеет абстрактный метод handle(args)

🔹 Команды

Каждая команда наследует Command и реализует handle:

```python
class Echo(Command):
    def handle(self, args=[]):
        print(*args)
        return self.current_path
```
🔹 main.py

    Разбирает аргументы командной строки

    Загружает VFS (zipfile)

    Считывает и выполняет скрипты

    Поддерживает ввод в интерактивном режиме

⚠️ Обработка ошибок

    Неизвестная команда в интерактиве:
    
    unknown cmd: test
    
    Неизвестная команда в скрипте:
    
    errors in script: test wrong
    
    Ошибки при чтении архива:

    Error reading tar file: <текст ошибки>

### 🔚 Завершение работы

Команда:

```bash
exit
```

завершает выполнение программы без ошибок.
