# Color Palette Guide

## Available Palettes

### 🟣 Viridis (Default)
```
#440154 → #482878 → #3E4989 → #31688E → #26828E → #1F9E89 → #35B779 → #6DCD59 → #B4DE2C → #FDE725
```
- **Perceptually uniform** — equal steps in color = equal steps in data
- **Colorblind safe** — works for all types of color vision
- **Best for**: Scientific data, heatmaps, sequential data, anything where accurate perception matters
- **Use when**: Data accuracy is paramount, professional/scientific context

### 🌅 Sunset
```
#3C1C2D → #6B2737 → #A0333F → #D44E50 → #F2784B → #F8A358 → #FBC96D → #F7F7B7 → #D9F0A3 → #A1DAB4
```
- Warm gradient from deep purple to soft green
- **Best for**: Marketing dashboards, growth metrics, energy/enthusiasm
- **Use when**: You want emotional warmth, storytelling data, growth narratives

### 🌊 Ocean
```
#011A3A → #013A63 → #0353A4 → #0AA6C2 → #2EC4B6 → #5BC0BE → #6FFFE9 → #5390D9 → #48BFE3 → #56CFE1
```
- Cool blues and teals
- **Best for**: Financial reports, corporate dashboards, calm/professional tone
- **Use when**: Business/corporate context, trust/reliability themes, financial data

### ⬛ Monochrome
```
#1a1a2e → #16213e → #1e2a45 → #2d3561 → #3a4373 → #4a5a8a → #5e72a4 → #7488b8 → #8da0cc → #a8b8e0
```
- Subtle grayscale-to-blue gradient
- **Best for**: Print-friendly reports, minimal design, executive summaries
- **Use when**: Data should speak for itself, print/PDF export, accessibility

### 💜 Neon
```
#FF006E → #FB5607 → #FFBE0B → #8338EC → #3A86FF → #06FFA5 → #00F5D4 → #FF4081 → #7B2FF7 → #F72585
```
- Vibrant, high-contrast, attention-grabbing
- **Best for**: Presentations, social media sharing, dashboards that need to pop
- **Use when**: Engagement matters, presentations, younger audiences, bold statements

## How to Choose

| Context | Recommended Palette |
|---------|-------------------|
| Scientific / Academic | Viridis |
| Business / Finance | Ocean |
| Marketing / Growth | Sunset |
| Executive / Print | Monochrome |
| Presentation / Viral | Neon |
| Heatmap | Viridis |
| Pie/Donut | Neon or Sunset |
| Line Chart (multi-series) | Ocean or Viridis |
| Dashboard | Ocean (professional) or Neon (engagement) |

## Usage

```bash
--palette viridis     # default
--palette sunset
--palette ocean
--palette monochrome
--palette neon
```

## Color Application Rules

1. **Sequential data** (time series, rankings): Use palettes in order (viridis, ocean)
2. **Categorical data** (pie, donut): High contrast palettes work best (neon, sunset)
3. **Multi-series**: Assign colors cyclically from the palette
4. **Single series**: First color of the palette
5. **Transparency**: Area fills use 20% opacity, bars use 80%, points use full opacity
