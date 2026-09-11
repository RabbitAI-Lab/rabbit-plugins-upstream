# Screenshot Organization Reference

## Platform-Specific Screenshot Patterns

| Platform | Filename Pattern | Default Location |
|----------|-----------------|------------------|
| macOS | `Screenshot 2026-01-15 at 10.30.00.png` | `~/Desktop/` or `~/Pictures/Screenshots/` |
| Windows | `Screenshot (1).png` | `~/Pictures/Screenshots/` |
| Windows (Snipping) | `Capture_2026-01-15-10-30-00.png` | `~/Pictures/` |
| Android | `Screenshot_20260115_103000_com.app.png` | `/sdcard/Pictures/Screenshots/` |
| iOS | `Screenshot_2026-01-15-10.30.00.png` or `IMG_1234.PNG` | Photos app |
| Linux (GNOME) | `Screenshot from 2026-01-15 10-30-00.png` | `~/Pictures/` |

## Content Categories

### How Screenshots are Classified

The categorizer uses keyword patterns in OCR-extracted text to classify screenshots:

| Category | Detection Keywords | Typical Content |
|----------|-------------------|-----------------|
| Chat/Social | "message", "sent", "received", emoji patterns | WhatsApp, iMessage, Slack, Discord |
| Receipt/Payment | "$", "total", "order", "payment", "invoice" | Shopping, banking, subscriptions |
| Error/Bug | "error", "failed", "exception", "crash", "stack trace" | App crashes, system errors |
| Document | long paragraphs, "chapter", "page" | Articles, ebooks, notes |
| Meme/Image | minimal text, known meme formats | Humor, reaction images |
| Code | "function", "class", "import", "def", "var" | Code snippets, terminal |
| Map/Location | "directions", coordinates, street names | Google Maps, locations |
| App Screenshot | app-specific UI elements | App settings, profiles |

## Perceptual Hashing for Deduplication

### How It Works

1. **MD5 Hash (exact duplicates):** Identical files have identical MD5 hashes. Fast and reliable for finding exact copies.

2. **Average Hash (near-duplicates):** 
   - Resize image to 8×8 grayscale
   - Compute average pixel value
   - Each pixel becomes 1 (above average) or 0 (below)
   - Creates 64-bit hash
   - Hamming distance between hashes = visual difference
   - Distance ≤ 5 = likely duplicate
   - Distance ≤ 10 = similar (may be cropped or edited)

3. **Confidence Scoring:**
   - Distance 0-2: 99% confidence (exact visual duplicate)
   - Distance 3-5: 90% confidence (near-duplicate, minor crop)
   - Distance 6-10: 75% confidence (similar, review needed)
   - Distance 11+: Different images

## OCR Extraction Details

### Text Quality Factors
- **Resolution:** Higher resolution = better OCR. Minimum 150 DPI recommended.
- **Contrast:** Dark text on light background works best.
- **Font size:** Text below 12px equivalent may not extract reliably.
- **Background:** Gradient or patterned backgrounds reduce accuracy.

### Entity Detection
The OCR extractor can identify:
- **URLs:** `https://example.com/path`
- **Email addresses:** `user@domain.com`
- **Phone numbers:** Various international formats
- **Dates:** Multiple date formats
- **Currency amounts:** `$123.45`, `€99,99`
- **Confirmation/Order numbers:** Patterns like `#ABC123`, `Order: 12345`

## Privacy Considerations

Screenshots often contain sensitive information:
- Passwords (temporary displays)
- Private messages
- Financial information (balances, account numbers)
- Personal identification

The search index stores all extracted text locally. Recommendations:
- Encrypt the index file
- Don't sync the index to cloud storage
- Consider running OCR on sensitive categories separately
- Review and redact before sharing organized screenshots
