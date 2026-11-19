# Configuration findings

- `APP_PORT=hello` has an invalid data type: the port must be a whole number.
- `DEBUG=true` violates the deployment policy requiring exactly `false`.
- `DB_PASSWORD` is empty. Password error messages must never contain its value.
- `dbhost` and `DB_HOST` describe the same concept, but only `DB_HOST` satisfies the contract. This file already contains a nonempty `DB_HOST`; the legacy key is redundant.

## Contract

1. `APP_PORT`: required integer between 1024 and 65535, inclusive.
2. `DEBUG`: required literal `false`, with exact case.
3. `DB_HOST`: required and nonempty; `dbhost` is not an alias.
4. `DB_PASSWORD`: required and nonempty; never display its value.

