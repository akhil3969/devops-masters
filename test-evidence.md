# Test evidence



## 1. Valid configuration

```sh
python3 validator.py valid.env.example
echo "Exit code: $?"
```


## 2. Original broken configuration

```sh
python3 validator.py messy.env
echo "Exit code: $?"
```



## 3. Port below the allowed range

```sh
python3 validator.py bad-port.env.example
echo "Exit code: $?"
```



## 4. Missing database host

```sh
python3 validator.py missing-host.env.example
echo "Exit code: $?"
```


