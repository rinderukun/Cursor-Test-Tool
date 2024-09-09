# Cursor Test Tool
Just a small program to test the state of the icon mouse cursor

### Create virtual venv:

```
python -m venv venv
```

```
venv\Scripts\activate
```

### Install PySide6

```
pip install PySide6
```

### Start project

```
python main.py 
```

## Build Exe

### Install 

```
pip install pyinstaller
```

### Build

Здесь `--onefile` указывает PyInstaller собрать все в один исполняемый файл. `your_script.py` - это основной Python файл вашего проекта. `--icon=app_icon.ico` - иконка. `--windowed` - только окно, без консольной строки. `--clean` очистит кэш. 

С иконкой
```
pyinstaller --clean --windowed --icon=icon.ico --add-data="icon.ico;." --name "Cursor Test Tool" main.py
```
