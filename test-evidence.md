# Test evidence — execution pending

Run each command from this folder. Record the actual output and exit code for each case:

```sh
python3 validator.py valid.env.example
echo "Exit code: $?"
python3 validator.py messy.env
echo "Exit code: $?"
python3 validator.py bad-port.env.example
echo "Exit code: $?"
python3 validator.py missing-host.env.example
echo "Exit code: $?"
python3 validator.py
echo "Exit code: $?"
```

In PowerShell, use `py` instead of `python3` and `$LASTEXITCODE` instead of `echo "Exit code: $?"`. Copy the actual output and exit status below after running each case. These are expected results, not observed results:

| Fixture | Expected output | Expected exit |
| --- | --- | --- |
| valid.env.example | Configuration accepted | 0 |
| messy.env | APP_PORT, DEBUG, DB_PASSWORD errors | 1 |
| bad-port.env.example | APP_PORT range error | 1 |
| missing-host.env.example | DB_HOST required error | 1 |
| No filename supplied | Usage message | 1 |

Check that no password value appears in the output. All supplied template passwords are dummy values.

## Peer review

- Reviewer and date: pending
- Reproduced test and actual result: pending
- Reviewer comment: pending
- Your code or test improvement in response: pending

Record the review and response, then commit the resulting code or test improvement.
