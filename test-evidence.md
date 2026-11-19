# Test evidence

Run from the folder containing `validator.py`. Replace each **Not recorded** entry with actual terminal output and its exit code. Expected results are guidance, not proof of execution.

## 1. Valid configuration

```sh
python3 validator.py valid.env.example
echo "Exit code: $?"
```

Expected: `Configuration accepted`, exit 0.

Actual output and exit code: **Not recorded**.

## 2. Original broken configuration

```sh
python3 validator.py messy.env
echo "Exit code: $?"
```

Expected: errors naming APP_PORT, DEBUG, and DB_PASSWORD, exit 1.

Actual output and exit code: **Not recorded**.

## 3. Port below the allowed range

```sh
python3 validator.py bad-port.env.example
echo "Exit code: $?"
```

Expected: APP_PORT range error, exit 1. Other required settings are valid.

Actual output and exit code: **Not recorded**.

## 4. Missing database host

```sh
python3 validator.py missing-host.env.example
echo "Exit code: $?"
```

Expected: DB_HOST required error, exit 1. Other required settings are valid.

Actual output and exit code: **Not recorded**.

## Optional: no filename

```sh
python3 validator.py
echo "Exit code: $?"
```

Expected: `Usage: python3 validator.py <config-file>`, exit 1.

Actual output and exit code: **Not recorded**.

In PowerShell, use `py` instead of `python3` and `$LASTEXITCODE` instead of the `echo` command. Check the status immediately after each Python command.

Password non-disclosure check: **Not recorded**. Confirm that error output contains no password values. Use only dummy credentials.

## Peer review of this work

- Reviewer and date: **Not recorded**.
- Review link or written comment: **Not recorded**.
- Negative test reproduced by reviewer, output, and exit code: **Not recorded**.
- Reviewer's feedback: **Not recorded**.
- Code or test improvement made in response: **Not recorded**.
- Follow-up commit: **Not recorded**.
