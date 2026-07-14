#!/usr/bin/env bash
# Rebuild the paper PDFs with Quarto.
#
# Usage:
#   ./build.sh all               # main paper + supplement + all journal variants
#   ./build.sh main              # paper/lol_circadian_rhythms.pdf
#   ./build.sh supp              # paper/lol_circadian_rhythms_supplement.pdf
#   ./build.sh variants          # all active journal variants
#   ./build.sh rsos              # a specific variant

set -euo pipefail

PAPER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/paper"
VARIANT_DIR="$PAPER_DIR/journal_variants"
# rsos (Royal Society Open Science) is the active submission variant.
# The bit, chb and gigascience variants are retired under
# journal_variants/archive/ and are no longer built.
VARIANTS=(rsos)

render() {
    echo "=== $1 ==="
    quarto render "$1" --to pdf
}

build_main() {
    render "$PAPER_DIR/lol_circadian_rhythms.qmd"
}

build_supp() {
    render "$PAPER_DIR/lol_circadian_rhythms_supplement.qmd"
}

build_variant() {
    local qmd="$VARIANT_DIR/lol_circadian_rhythms_$1.qmd"
    if [[ ! -f "$qmd" ]]; then
        echo "Unknown variant '$1' (expected one of: main ${VARIANTS[*]})" >&2
        exit 1
    fi
    render "$qmd"
}

if [[ $# -eq 0 ]]; then
    grep '^#   ' "${BASH_SOURCE[0]}" | sed 's/^#   //'
    exit 1
fi

for target in "$@"; do
    case "$target" in
        all)
            build_main
            build_supp
            for v in "${VARIANTS[@]}"; do build_variant "$v"; done
            ;;
        variants)
            for v in "${VARIANTS[@]}"; do build_variant "$v"; done
            ;;
        main)
            build_main
            ;;
        supp)
            build_supp
            ;;
        *)
            build_variant "$target"
            ;;
    esac
done
