#!/usr/bin/env bash
set -euo pipefail

echo "[migration-smoke] Starting Alembic migration smoke test"

# Use a local SQLite DB to verify that migrations can run end-to-end in CI.
export DATABASE_URL="${DATABASE_URL:-sqlite+aiosqlite:///./ci_migration_smoke.db}"

alembic upgrade head
alembic current

echo "[migration-smoke] Migration smoke test completed successfully"
