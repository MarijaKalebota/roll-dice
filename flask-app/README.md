## Flask Instructions

## Setup

```bash
python3 -m pip install -r requirements.txt --user
```

## Run

```bash
python3 -m flask run
```

## Test

```bash
python3 -m pytest
```

## Build

```bash
python3 setup.py sdist bdist_wheel
```
This will create distributions in the "dist" folder. The "sdist" part will create a source archive (.tar.gz), and the "bdist_wheel" part will create a built distribution in the "wheel" form (as opposed to an "egg" form).