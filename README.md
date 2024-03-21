# BootModule

## Оглавление  
[1. Описание проекта](./README.md#Описание-проекта)   
[2. Как установить и запустить проект](./README.md#Как-установить-проект)  
[3. Данные для запуска проекта](./README.md#Данные-для-запуска-проекта)

### Описание проекта    
Гибридное приложение для администрирования и функционирования устройства "Тонкий клиент" (одноплатный компьютер - Rock Pi/Raspberry Pi) под ОС Linux (Ubuntu/Debian). Так же имеется WebView для загрузки веб-страницы и удаленного администрирования устройства через нее. Позволяет выбрать/задать следующие параметры:
1. Ethernet - настроить статический или динамический IP. Либо выбрать Wi-Fi.
2. Подключить VPN.
3. Сменить пародь администратора к данному устройству.
4. Выбрать подключение к удаленному рабочему столу или режим Web-киоска.

### Как установить и запустить проект
Выполнить следующие команды в терминале (у меня - VS Code):
1. git clone https://github.com/NadezdaNN/BootModule
2. Установить зависимости: pip install -r requirements.txt
3. Приложение запускается на одноплатном компьютере или виртуальной машине с установленной ОС (Ubuntu/Debian), выполнением команды в терминале: sudo ./main.py

### Данные для запуска проекта
1. После загрузки логотипа в течение 5 сек. нажать F2 для доступа к настройкам.
2. Ввести пароль администратора: 123
3. На форме настроек ввести необходимые параметры и сохранить их. Далее, вернуться к загрузке логотипа по кнопке ESC и дождаться подключения к удаленному рабочему столу или web-киоску.
4. На форме ввода пароля администратора возможно сбросить все настройки, удерживая клавишу F10 в течение 5 секунд.
