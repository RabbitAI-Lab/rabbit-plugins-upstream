# Icon library

## Lucide-style generic icons

Use simple 24-unit inline SVG geometry for generic interface symbols. Keep
`fill="none"`, `stroke="currentColor"`, rounded line caps, and a 1.5–2
stroke width. Rebuild only the paths the composition needs; do not use an icon
font, emoji, dingbat, or Unicode arrow.

Common choices for OG cards:

- search: circle plus diagonal handle
- play: outlined circle plus a small triangular path
- check: two-stroke path inside a rounded square
- trend: three connected points with an SVG arrowhead path
- spark: four short tapered paths around a center point
- book: two mirrored open-page paths

## LobeHub marks

Use a monochrome LobeHub brand mark only when the card describes a real AI
integration. Pair it with a visible text label, preserve its geometry, and do
not use it as the fictional brand's logo or as decoration.

## Generated-image rule

Describe any generic icon as line geometry in the prompt. If the generator
turns it into an emoji or a recognizable third-party logo, reject the result
and revise the prompt before requesting another paid image.
