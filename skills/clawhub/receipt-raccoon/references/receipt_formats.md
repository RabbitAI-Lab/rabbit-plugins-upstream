# Supported Receipt Formats

Receipt Raccoon is designed to handle the "messy text" that comes out of OCR tools and manual transcription.

## What Works Well

### Standard grocery receipt
```
WHOLE FOODS MARKET #12345
123 Organic Street, Portland, OR 97201
01/15/2024  14:32

ORGANIC BANANAS       2.99
ALMOND MILK           3.49
FREE RANGE EGGS       5.99

SUBTOTAL             49.93
TAX                   4.00
TOTAL                53.93
```

### Restaurant receipt
```
OLIVE GARDEN #234
Jan 20, 2024

LASAGNA              16.99
COCA COLA             2.99
TIRAMISU              7.49
TIP                   5.00

SUBTOTAL             27.47
TAX                   2.20
TOTAL                34.67
```

### Gas station receipt
```
SHELL STATION #5678
02/01/2024

UNLEADED 10.326 GAL  34.99

SUBTOTAL             34.99
TOTAL                34.99
```

## Parsing Logic

### Merchant Detection
- The merchant is taken from the **first meaningful line** (non-date, non-phone-number).
- Lines 1-5 are scanned. Lines with only numbers, dates, or phone numbers are skipped.

### Date Detection
Multiple date formats are recognised:
- `2024-01-15` (ISO)
- `01/15/2024` or `1/15/24` (US slash)
- `15.01.2024` (EU dot)
- `Jan 15, 2024` or `January 15 2024` (written)
- `15 Jan 2024` (day-first written)

The first valid date found anywhere in the text is used.

### Item Detection
A line is treated as a line item if:
1. It contains a monetary value (pattern: `XX.XX` or `$XX.XX`)
2. It is NOT a summary line (subtotal, tax, total, tip)
3. It does NOT contain skip keywords (phone, address, card info, etc.)

The item name is extracted as everything before the price, cleaned up by:
- Removing leading item numbers (e.g., `1 BANANA` → `BANANA`)
- Removing trailing quantities
- Trimming extra whitespace and special characters

### Summary Line Detection
Lines containing these keywords are treated as summary lines:
- **Subtotal:** "subtotal", "sub total", "sub-total"
- **Tax:** "tax", "vat", "gst", "hst", "pst", "sales tax"
- **Total:** "total", "balance due", "amount due", "grand total"
- **Tip:** "tip", "gratuity"

### Fallback Logic
- If no subtotal is found, it's calculated by summing all line items.
- If no total is found, it's calculated as subtotal + tax.

## Limitations

### OCR Errors
The parser is fairly robust to whitespace variations but cannot fix garbled OCR text. For best results:
- Ensure the OCR output has one item per line
- Fix obvious character recognition errors before parsing

### Multi-line Items
Items that span multiple physical lines (e.g., long product names that wrap) may be split into two items. The parser treats each line independently.

### BOGO and Discounts
"Buy one get one" offers, percentage discounts, and loyalty point redemptions on their own line are typically skipped (they contain keywords like "discount", "savings", "reward"). Negative-value discount lines are also handled.

### Currency
All amounts are assumed to be in USD. The `currency` field is set to "USD" by default. To support other currencies, modify the `parse_receipt` function.

### Multi-item Quantities
Lines like `3 x BANANA @ 0.99` may not parse perfectly. The parser looks for a single price at the end of each line.

## Tips for Best Results

1. **One item per line** — Most receipt OCR output already follows this.
2. **Include dates** — Helps with monthly reporting.
3. **Keep summary keywords clear** — "SUBTOTAL", "TAX", "TOTAL" should be present.
4. **Remove non-receipt text** — Conversational text from voice/photo descriptions should be cleaned before parsing.
