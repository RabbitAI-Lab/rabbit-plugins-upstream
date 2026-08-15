# Template Reference Guide

This document describes how each meme template works, what the visual layout looks like, and when to use it.

## Template Overview

All templates render at **800×800** SVG units and are drawn entirely with SVG shapes (rects, circles, paths, gradients). No raster images are embedded.

---

## 1. Drake (`drake`)

**Layout**: Two horizontal panels stacked vertically. Left side has a stylized figure (rejecting on top, approving on bottom). Right side has text.

**Text positions**: Top text on right of upper panel, bottom text on right of lower panel.

**When to use**: Comparing two options where one is clearly better. The "reject then approve" pattern.

**Example**: 
- Top: "WRITING TESTS" (rejected)
- Bottom: "COPY-PASTING FROM STACK OVERFLOW" (approved)

---

## 2. Distracted Boyfriend (`distracted_boyfriend`)

**Layout**: Three character silhouettes — boyfriend in center turning head, girlfriend on left, distraction on right. Labels float above each character.

**Text positions**: Top text over the scene, labels on each character area.

**When to use**: Showing divided attention, temptation, or choosing one thing over another.

**Example**:
- Top: "DEADLINES" (girlfriend)
- Bottom: "NEW SIDE PROJECT" (distraction)
- Center: "ME"

---

## 3. Two Buttons (`two_buttons`)

**Layout**: A figure with hand extended toward two large buttons. Left button = top text, right button = bottom text. Sweat drop indicates anxiety.

**Text positions**: Text inside each button.

**When to use**: An impossible dilemma, two equally tempting/terrifying options.

**Example**:
- Left: "SHIP IT NOW"
- Right: "WRITE TESTS FIRST"

---

## 4. Change My Mind (`change_my_mind`)

**Layout**: A figure sitting at a folding table with a sign. The sign contains the main text.

**Text positions**: Top text at top of image, text repeated on the sign.

**When to use**: Stating a controversial opinion you're daring others to challenge.

**Example**:
- "PYTHON IS THE BEST LANGUAGE"

---

## 5. Galaxy Brain (`galaxy_brain`)

**Layout**: Five brain shapes arranged vertically, each progressively brighter/glowing, set against a starry space background.

**Text positions**: Labels beside the first (dumbest) and last (smartest) brain.

**When to use**: Showing an escalation of ideas from basic to mind-blowing.

**Example**:
- Bottom (dumb): "USE TABS"
- Top (genius): "NEITHER — WRITE BINARY"

---

## 6. Stonks (`stonks`)

**Layout**: Suit-wearing figure on the left, with a green upward-pointing line graph and "STONKS" text on the right. Dark blue financial background.

**Text positions**: Top text at top, bottom text at bottom.

**When to use**: Ironic celebration of something going up that shouldn't, or financial humor.

**Example**:
- Top: "BUY HIGH"
- Bottom: "SELL LOW"

---

## 7. This is Fine (`this_is_fine`)

**Layout**: Cartoon dog sitting at a table with a coffee mug, surrounded by orange/yellow flames. Warm orange background.

**Text positions**: Standard top/bottom Impact text.

**When to use**: Accepting a terrible situation with false calm. Denial humor.

**Example**:
- Top: "PRODUCTION DOWN"
- Bottom: "THIS IS FINE"

---

## 8. Doge (`doge`)

**Layout**: Shiba Inu dog on a cream/beige background. Multiple colorful Comic Sans labels scattered around ("WOW", "SUCH", "VERY", etc.).

**Text positions**: Top text combined with doge-speak labels, bottom text in Impact style.

**When to use**: Playful, ironic praise. Anything that deserves a "much wow."

**Example**:
- Top: "CLEAN CODE"
- Bottom: "VERY READABLE"

---

## 9. Expanding Brain (`expanding_brain`)

**Layout**: Four brain silhouettes arranged vertically, each with increasing brightness/glow. Divided by horizontal lines into stages.

**Text positions**: Labels for the first (basic) and last (enlightened) stages.

**When to use**: Escalating cleverness from obvious to brilliant/absurd.

**Example**:
- Top (basic): "COMMENT YOUR CODE"
- Bottom (galaxy): "THE CODE COMMENTS ITSELF"

---

## 10. Panik Kalm Panik (`panik_kalm`)

**Layout**: Three vertical panels — left (red, PANIK), center (blue, KALM), right (red, PANIK). Animated pulsing circles in panic panels, calm face in center.

**Text positions**: Text at top of each panel, PANIK/KALM labels at bottom.

**When to use**: A situation where you panic, briefly calm down, then realize something worse and panic again.

**Example**:
- Left: "BUG IN PRODUCTION"
- Center: "OH WAIT, IT'S FRIDAY"
- Right: "FRIDAY DEPLOY"

---

## Custom Templates

Create your own SVG template with `{{TOP}}` and `{{BOTTOM}}` placeholders:

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800">
  <rect width="800" height="800" fill="#gradient_or_color"/>
  <!-- Your custom shapes/paths here -->
  {{TOP}}
  {{BOTTOM}}
</svg>
```

The generator will replace placeholders with properly styled Impact text blocks (white fill, black stroke, uppercase, word-wrapped).

### Custom Template Guidelines

- **Canvas**: 800×800 viewBox recommended
- **Background**: Always include a background rect
- **Placeholders**: `{{TOP}}` and `{{BOTTOM}}` — these get replaced with full `<text>` elements
- **Colors**: Use SVG-compatible color names or hex codes
- **Gradients**: Define in `<defs>` and reference with `url(#id)`
