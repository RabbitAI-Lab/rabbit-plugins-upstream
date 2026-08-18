# SVG Text Rendering Guide

How text is rendered in meme SVGs — styling, wrapping, and animation tricks.

## Impact Font Stack

The classic meme look uses **Impact** font. Since Impact may not be available on all systems, we use a font stack:

```css
font-family: Impact, 'Arial Black', Haettenschweiler, sans-serif
```

This cascades: if Impact isn't installed, the browser tries Arial Black, then Haettenschweiler, then a generic sans-serif. On most Windows systems Impact is pre-installed; on Linux/macOS, Arial Black is the common fallback.

## Text Styling

### White Fill + Black Stroke (Classic Meme Look)

```xml
<text x="400" y="65"
      font-family="Impact, 'Arial Black', sans-serif"
      font-size="60"
      font-weight="bold"
      fill="white"
      stroke="black"
      stroke-width="4"
      stroke-linejoin="round"
      stroke-linecap="round"
      paint-order="stroke fill"
      text-anchor="middle"
      letter-spacing="1.5">
  TOP TEXT
</text>
```

### Key Attributes

| Attribute | Value | Purpose |
|---|---|---|
| `fill` | `white` | Interior text color |
| `stroke` | `black` | Outline color |
| `stroke-width` | `3–5` | Outline thickness (scales with font size) |
| `paint-order` | `stroke fill` | Draw outline BEHIND fill (critical!) |
| `stroke-linejoin` | `round` | Rounded corners on outline |
| `font-weight` | `bold` | Extra thickness |
| `letter-spacing` | `1.5` | Slight spacing for readability |
| `text-anchor` | `middle` | Horizontal centering |

### Why `paint-order="stroke fill"`?

Without this, the stroke is drawn ON TOP of the fill, making text look thin/hollow. With `stroke fill` order, the stroke renders first (as a fat outline), then the white fill paints over its center, leaving a clean black border.

This is the single most important attribute for authentic meme text.

## Text Wrapping

SVG `<text>` doesn't auto-wrap. We manually split long text into multiple `<text>` elements with calculated Y positions.

### Wrapping Algorithm

```python
def wrap_text(text, max_chars=22):
    """Split text into lines of at most max_chars."""
    lines = []
    for word in text.split():
        if not lines or len(lines[-1]) + 1 + len(word) > max_chars:
            lines.append(word)
        else:
            lines[-1] += " " + word
    return lines
```

### Line Height

Each line is offset by `font_size * 1.05` vertically:

```python
line_height = font_size * 1.05
for i, line in enumerate(lines):
    y = base_y + i * line_height
```

### Auto-sizing

The generator shrinks font size until the longest line fits within the canvas width:

```python
def optimal_font_size(lines, max_width_ratio=0.92, base_size=60, min_size=22):
    longest = max(len(line) for line in lines)
    while base_size > min_size:
        char_width = base_size * 0.52  # Impact avg char width ratio
        if longest * char_width <= WIDTH * max_width_ratio:
            return base_size
        base_size -= 2
    return min_size
```

The `0.52` ratio approximates the average character width relative to font size for Impact/Arial Black (wider than normal fonts).

## Positioning

### Top Text
```python
y_start = 65  # Fixed top padding
y = y_start  # First line baseline
```

### Bottom Text
```python
total_height = num_lines * font_size * 1.05
y_start = HEIGHT - total_height - 25  # 25px bottom padding
```

### Center Text
```python
total_height = num_lines * font_size * 1.05
y_start = (HEIGHT - total_height) / 2 + font_size
```

## Animation

SVG supports native CSS/SMIL animations without JavaScript.

### Fade-In Effect

```xml
<text ...>
  TEXT
  <animate attributeName="opacity"
           values="0;1"
           dur="0.4s"
           begin="0.2s"
           fill="freeze"/>
</text>
```

- `values="0;1"` — fade from 0% to 100% opacity
- `dur="0.4s"` — animation duration
- `begin="0.2s"` — delay before start (stagger lines)
- `fill="freeze"` — hold final state (don't reset)

### Pulsing Effect (Panik)

```xml
<circle ...>
  <animate attributeName="r"
           values="40;80;40"
           dur="1.5s"
           repeatCount="indefinite"/>
  <animate attributeName="opacity"
           values="0.5;0;0.5"
           dur="1.5s"
           repeatCount="indefinite"/>
</circle>
```

### Reduced Motion Accessibility

Always respect user preferences:

```xml
<style>
  @media (prefers-reduced-motion: reduce) {
    animate { display: none; }
  }
</style>
```

## Export to HTML

For easy browser viewing, wrap SVG in a minimal HTML page:

```html
<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; display: flex; justify-content: center;
         align-items: center; min-height: 100vh; background: #1a1a2a; }
  svg { max-width: 100%; height: auto; }
</style>
</head>
<body>
  <!-- SVG content here -->
</body>
</html>
```

The `max-width: 100%` makes the SVG responsive — it scales to fit any screen.

## Common Issues

### Text appears behind shapes
Add text AFTER shapes in the SVG document (later elements render on top).

### Font looks wrong on Linux
Install `fonts-liberation` or `ttf-mscorefonts-installer` for Impact. Alternatively, Arial Black is usually available.

### Stroke makes text too thin
Ensure `paint-order="stroke fill"` is set. Without it, the stroke covers half the fill.

### Text too wide
Reduce `max_chars` in the wrapping function, or let `optimal_font_size` auto-shrink.
