#!/usr/bin/env bash
# Stage a clean, shareable deposit/ folder for the public archive (e.g. Zenodo/GitHub).
#
# Includes: analysis code + all de-identified, aggregated outputs needed to
#           reproduce every figure in the paper.
# Excludes: per-account selection lists (top_players_*.csv) that carry raw Riot
#           ACCOUNTIDs, plus any local database/cache state. No raw match records
#           or raw MMR values exist outside the proprietary store, so none leak here.
#
# Re-run any time:  ./make_deposit.sh
set -euo pipefail
cd "$(dirname "$0")"

DEST="deposit"

# Optional: drop the three non-analysed/beta servers from the deposit.
# Leave empty to include everything. Example: EXCLUDE_SERVERS=(ID1 TR1 PBE1)
EXCLUDE_SERVERS=()

rm -rf "$DEST"
mkdir -p "$DEST"

# Analysis code
cp riot_analysis.py grand_analysis.py "$DEST"/

# Build rsync exclude list
excludes=(
  --exclude='top_players_*.csv'
  --exclude='*.duckdb' --exclude='*.duckdb.wal'
  --exclude='*.db' --exclude='*.sqlite'
  --exclude='__pycache__/'
)
for s in "${EXCLUDE_SERVERS[@]:-}"; do
  [ -n "$s" ] && excludes+=( --exclude="$s/" )
done

# Copy derived outputs from disk (not git) so per-server folders are included too
rsync -a --prune-empty-dirs "${excludes[@]}" results/ "$DEST"/results/

# Safety net: refuse to ship anything carrying an account identifier
if grep -rIli --exclude='*.py' -e accountid -e puuid -e summoner -e account_id "$DEST" >/dev/null; then
  echo "ABORT: identifier-bearing file found in $DEST/ :" >&2
  grep -rIli --exclude='*.py' -e accountid -e puuid -e summoner -e account_id "$DEST" >&2
  rm -rf "$DEST"
  exit 1
fi

echo "Clean deposit staged in ./$DEST/"
echo "files: $(find "$DEST" -type f | wc -l)"
