#!/usr/bin/env bash
# Sample invocations for repair_or_replace.py
# Run with: bash scripts/sample_run.sh

SCRIPT="scripts/repair_or_replace.py"
echo "============================================="
echo "Example 1: Old Washing Machine"
echo "============================================="
python3 "$SCRIPT" \
    --item "washing machine" \
    --age 8 \
    --repair-cost 250 \
    --replacement-cost 800 \
    --expected-lifespan 12 \
    --symptoms "won't spin during cycle" \
    --condition 5

echo ""
echo "============================================="
echo "Example 2: Broken Laptop (borderline)"
echo "============================================="
python3 "$SCRIPT" \
    --item "laptop" \
    --age 5 \
    --repair-cost 450 \
    --replacement-cost 900 \
    --expected-lifespan 5 \
    --symptoms "screen flickering, battery dies fast" \
    --condition 4

echo ""
echo "============================================="
echo "Example 3: Vintage Watch (sentimental)"
echo "============================================="
python3 "$SCRIPT" \
    --item "mechanical watch" \
    --age 20 \
    --repair-cost 150 \
    --replacement-cost 500 \
    --expected-lifespan 40 \
    --sentimental 9 \
    --condition 7

echo ""
echo "============================================="
echo "Example 4: Old Fridge (efficiency gain)"
echo "============================================="
python3 "$SCRIPT" \
    --item "refrigerator" \
    --age 14 \
    --repair-cost 350 \
    --replacement-cost 1000 \
    --expected-lifespan 14 \
    --symptoms "not cooling properly, noisy" \
    --condition 3 \
    --efficiency-gain 35

echo ""
echo "============================================="
echo "Example 5: JSON Output"
echo "============================================="
python3 "$SCRIPT" \
    --item "television" \
    --age 6 \
    --repair-cost 200 \
    --replacement-cost 600 \
    --expected-lifespan 7 \
    --format json
