# BAB 10 - pip & Virtual Environment

Jalankan perintah ini di **Terminal** VS Code (bukan di file .py).

## Buat & aktifkan virtual environment

Mac / Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```
python -m venv .venv

```

## Install paket dari PyPI
```
pip insta.venv\Scripts\Activate.ps1ll pandas requests
```

## Simpan & pasang ulang dependensi
```
pip freeze > requirements.txt
pip install -r requirements.txt
```
