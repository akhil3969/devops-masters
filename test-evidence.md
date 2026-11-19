# Test evidence — execution pending

On 2026-11-19, `python3 validator.py messy.env` could not start Python:

```text
xcode-select: error: No developer tools were found and no install could be requested (possibly because there is no active GUI session).
```

The shell reported status 1 from the unavailable launcher. This is an environment failure, not evidence of validator rejection. The scaffold's intentional `NotImplementedError` could not be observed either.

After installing/configuring Python 3, run each command from this folder. The line immediately after each test displays its exit code:

```sh
python3 validator.py valid.env.example
echo "Exit code: $?"
python3 validator.py messy.env
echo "Exit code: $?"
python3 validator.py bad-port.env.example
echo "Exit code: $?"
python3 validator.py missing-host.env.example
echo "Exit code: $?"
```

In PowerShell, use `py` instead of `python3` and `$LASTEXITCODE` instead of `echo "Exit code: $?"`. Copy the actual output and exit status below after running each case. These are expected results, not observed results:

| Fixture | Expected output | Expected exit |
| --- | --- | --- |
| valid.env.example | Configuration accepted | 0 |
| messy.env | APP_PORT, DEBUG, DB_PASSWORD errors | 1 |
| bad-port.env.example | APP_PORT range error | 1 |
| missing-host.env.example | DB_HOST required error | 1 |

Check that no password value appears in the output. All supplied template passwords are dummy values.

## Git and peer review — pending

Use the existing repository; do not initialize a nested repository. Git was also unavailable during the initial attempt because macOS Command Line Tools were missing. No branch or commits were created by the assistant.

After capturing actual test results, run:

```sh
git status
git switch -c class02-config-validator
git add validator.py valid.env.example bad-port.env.example missing-host.env.example findings.md test-evidence.md
git commit -m "Validate application configuration"
```

Ask a classmate to reproduce the bad-port test and suggest a meaningful improvement, such as checking the port boundaries. Record the actual review:

- Reviewer and date: pending
- Reproduced test and actual result: pending
- Reviewer comment: pending
- Your code or test improvement in response: pending

Make the improvement, rerun the affected tests, update this evidence, then commit the changed files with `git commit -m "Address peer review feedback"` after staging them. Do not invent reviewer feedback or test results.
