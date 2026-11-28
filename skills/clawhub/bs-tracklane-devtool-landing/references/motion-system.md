# Motion system

Motion explains the product and confirms actions. It is calm, plays once, and
never hides content.

## Tokens

| Token | Value | Use |
| --- | --- | --- |
| `--ease-out` | `cubic-bezier(.23,1,.32,1)` | Entrances, reveals, popovers, switches |
| `--ease-in-out` | `cubic-bezier(.77,0,.175,1)` | On-screen movement (FLIP card move) |
| `--ease-drawer` | `cubic-bezier(.32,.72,0,1)` | Mobile sheet |
| `--d-1` | 140ms | Hover, press, color |
| `--d-2` | 220ms | Menus, tabs, switches, header backdrop |
| `--d-3` | 640ms | Scroll reveals |

Press feedback: `transform: scale(.97)` on buttons, chips and cards on
`:active`. Animate only `transform` and `opacity` (plus `grid-template-rows` for
accordions and collapsing triage rows, and `stroke-dashoffset` for chart lines).

## What animates and why

| Element | Motion | Why |
| --- | --- | --- |
| Hero copy | Rise 10px + fade, 560ms, 50ms stagger, on load (done by 0.8s) | Calm entrance; headline first, nothing stays hidden |
| Product frame | Rise 14px + fade, 700ms, 120ms delay (done by 0.82s) | Brings in the product without a zoom or bounce |
| Hero view indicator | Active bar fills (7.8s board, 6.4s others), then advances; one loop only, then rests on Board with a solid bar | Shows the three views without a click; stops so it never competes with reading |
| Board card move | After 2.6s visible, PLT-488 slides Todo to In progress (FLIP, 820ms), siblings reflow (520ms), in-app toast for 3.4s; once | Explains the core promise: code activity updates status |
| Burn-up / roadmap | Lines draw (1.1s), bars grow from 20% (800ms, 70ms stagger) when the view enters | State transition, reads as live data |
| Section reveals | Fade + 18px rise, 640ms, 70ms stagger via `--i`, once | Rhythm while scrolling |
| Metric numbers | Count up over 1.2s when 60% visible, once | Draws the eye to the claim |
| Triage rows | Collapse (grid rows 1fr to 0fr, 360ms) + fade on accept/snooze/decline | Feedback; the queue visibly shrinks |
| Cycles tabs | Progress bar along the active tab (8s), advances once through all four while visible | Guides through the four capabilities |
| Panels and routes | Fade + 6px rise, 320 to 460ms | Prevents jarring swaps |
| Velocity bars | Scale Y from the baseline, 640ms with 40ms stagger, on range change | Shows the data changed |
| Billing switch | Thumb slides (320ms), prices roll out up and in from below (420ms) | Confirms which price is shown |
| Workflow feed | Three events light up 650ms apart when visible, once | Narrates branch, review, merge |
| Marquee | 46s linear loop, pauses on hover | The only perpetual motion; far from body copy |
| Accordions | Grid rows 0fr to 1fr, 360ms; plus icon rotates to minus | Height change without layout jank |
| Toasts | Rise 10px + fade in, out after 3.2s | Feedback after actions |

## Reveal pattern with fallback

1. A head script adds `class="js"` to `<html>`. Reveal styles exist only under
   `.js`, so without JavaScript everything is visible.
2. An `IntersectionObserver` (threshold .06, bottom margin -6%) adds `.is-in`
   once and unobserves. If `IntersectionObserver` is missing, or reduced motion
   is on, every `.reveal` gets `.is-in` immediately. A `beforeprint` handler
   reveals everything for printing.
3. The hero never waits for scroll; it animates on load.
4. Carousel slides that are not active use `hidden` (not opacity), so no text is
   ever stuck invisible.

## Pausing rules

Auto-advancing tabs pause (CSS `animation-play-state`) while the pointer is over
the component, while focus is inside it, while it is offscreen and while the
document is hidden. Any click on a tab stops auto-advance for good. The live
card move only fires when the board is visible and the tab is in front.

## Reduced motion

`@media (prefers-reduced-motion: reduce)` collapses every animation and
transition to 1ms, makes reveals instant, stops the marquee and wraps the
wordmarks into a static row, shows the workflow feed fully, and smooth scrolling
becomes instant. JavaScript also checks the preference: no auto-advance, no
count-up, no card move, no WAAPI bar growth. Color and opacity feedback (hover,
selected states, toasts) remain.
