# Knitting Pattern Notation Reference

## Standard Abbreviations

The parser recognizes these standard abbreviations used across English-language knitting patterns:

### Basic Stitches
| Abbrev | Meaning | Stitch Delta |
|--------|---------|-------------|
| k / K | knit | 0 |
| p / P | purl | 0 |
| sl | slip stitch | 0 |

### Increases
| Abbrev | Meaning | Stitch Delta |
|--------|---------|-------------|
| yo | yarn over | +1 |
| m1 / m1l / m1r | make one | +1 |
| kfb / kf&b | knit front and back | +1 |
| pfb | purl front and back | +1 |
| k1f&b | knit front and back | +1 |

### Decreases
| Abbrev | Meaning | Stitch Delta |
|--------|---------|-------------|
| k2tog | knit two together | -1 |
| p2tog | purl two together | -1 |
| ssk | slip, slip, knit | -1 |
| ssp | slip, slip, purl | -1 |
| k3tog | knit three together | -2 |
| sk2po | slip 1, knit 2 together, pass slip st over | -2 |
| cdd | centered double decrease | -2 |

### Casting
| Abbrev | Meaning | Effect |
|--------|---------|--------|
| co / CO | cast on | sets initial stitch count |
| bo / BO / bind off | bind off | -1 per stitch bound off |

### Repeat Notation

Patterns use asterisks to mark repeat sections:

- `* k2, p2, rep from * to end` — repeat the section between `*` and `rep from *` until you run out of stitches
- `* k2, p2, rep from * 3 times` — repeat the section exactly 3 more times (4 total executions)
- `* k2, p2, rep from * to last 4 sts` — repeat until 4 stitches remain
- `[k2, p2] 4 times` — bracket-style repeat, 4 total times
- `(k2, p2) 3 times` — parenthesis-style repeat, 3 total times

### Stitch Delta Logic

For any instruction segment, the parser computes net stitch delta:

```
Net delta = sum of all individual stitch deltas in the segment
```

For a repeat:
```
Total delta = per-repeat delta × number of repeats
```

### Yarn Calculation Formula

Given:
- `Gs` = gauge stitches per 4 inches
- `Gr` = gauge rows per 4 inches  
- `Sy` = yards consumed by the swatch (typically a 4"×4" square)
- `Ps` = project total stitches across width
- `Pr` = project total rows

The calculation:
```
Swatch stitch-units = Gs × Gr
Project stitch-units = Ps × Pr
Area ratio = Project stitch-units / Swatch stitch-units
Estimated yards = Sy × Area ratio
Recommended yards = Estimated yards × (1 + buffer)
```

Standard buffer: 15% (accounts for tension variation, swatching error, and seaming).

### Skein Size Reference

Common skein sizes for yardage conversion:
- Sock/Fingering: ~400-460 yd per 100g
- DK/Light Worsted: ~220-280 yd per 100g
- Worsted: ~180-220 yd per 100g
- Bulky: ~120-150 yd per 100g
- Super Bulky: ~80-100 yd per 100g

## Common Pattern Structures

### Ribbing
```
*k2, p2, rep from * to end
```
Net change: 0. Must divide evenly into cast-on count.

### Lace (balanced)
```
*k2tog, yo, rep from * to end
```
Net change per repeat: 0. Creates eyelets.

### Decrease row (shaping)
```
*k6, k2tog, rep from * to end
```
Net change: -1 per repeat × (total/8) repeats.

### Cable setup
```
*p2, k4, p2, rep from * to end
```
8-stitch repeat, net change: 0.
