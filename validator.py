import sys


def validate(values):
    errors = []
    try:
        port = int(values.get("APP_PORT", ""))
    except ValueError:
        errors.append("APP_PORT must be a whole number between 1024 and 65535")
    else:
        if not 1024 <= port <= 65535:
            errors.append("APP_PORT must be between 1024 and 65535 (inclusive)")
    if values.get("DEBUG") != "false":
        errors.append("DEBUG must be exactly false")
    for key in ("DB_HOST", "DB_PASSWORD"):
        if not values.get(key, "").strip():
            errors.append(f"{key} must be present and nonempty")
    return errors


def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 validator.py <config-file>", file=sys.stderr)
        sys.exit(1)
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
