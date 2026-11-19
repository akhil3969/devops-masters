# Test evidence



## 1. Valid configuration

```sh
python3 validator.py valid.env.example
echo "Exit code: $?"
```
echo "Exit code: $?"
Configuration accepted
Exit code: 0

## 2. Original broken configuration

```sh
python3 validator.py messy.env
echo "Exit code: $?"
```

echo "Exit code: $?"
APP_PORT must be a whole number between 1024 and 65535
DEBUG must be exactly false
DB_PASSWORD must be present and nonempty
Exit code: 1

## 3. Port below the allowed range

```sh
python3 validator.py bad-port.env.example
echo "Exit code: $?"
```

onasaiakhil@konas-MacBook-Air devops-masters % python3 validator.py bad-port.env.example
echo "Exit code: $?"
APP_PORT must be between 1024 and 65535 (inclusive)
Exit code: 1
konasaiakhil

## 4. Missing database host

```sh
python3 validator.py missing-host.env.example
echo "Exit code: $?"
```
cho "Exit code: $?"
DB_HOST must be present and nonempty
Exit code: 1

