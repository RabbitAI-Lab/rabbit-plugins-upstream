# course-module · 教学模块

7-slide teaching module: cover (title + meta), objectives, core concept, worked example, exercise, check-your-understanding (MCQ), summary.

Academic but friendly look: warm off-white paper, Playfair Display display type, a green/terracotta accent pair. A persistent **left sidebar** on content slides lists the module's learning objectives and checks them off as you progress — students always know where they are.

**Use when:** online course modules, lecture handouts, onboarding curricula, workshop units.
**Feel:** a good textbook opened to a chapter — structured, quiet, encouraging.

## Images

This template provides the following CSS classes for image placement:

| Class | Where | Layout |
|-------|-------|--------|
| `.cover-img` | Cover / summary slides (`.slide.full`) | Absolutely positioned right side, vertically centered. Apply **directly on `<img>`** — no wrapper div |
| `.img-hero` | Main content area (`.main`) | Full-width block between text sections. Apply **directly on `<img>`** — no wrapper div |
| `.img-float-right` | Main content area (`.main`) | Floating right with text wrapping. Apply **directly on `<img>`** — no wrapper div |
| `.img-float-left` | Main content area (`.main`) | Floating left with text wrapping. Apply **directly on `<img>`** — no wrapper div |
| `.framed-img` | Main content area (`.main`) | Image with visual framing directly on `<img>`, plus standalone `.framed-caption` below |
| `.img-card` | Inside `.concept-box` | Full-width at card top, border-radius on img directly. Crop via `clip-path: inset(...)` if needed |
| `.img-float-right` | Main content area (`.main`) | Floating right with text wrapping. Applied **directly to `<img>`** (no wrapper). |
| `.img-float-left` | Main content area (`.main`) | Floating left with text wrapping. Applied **directly to `<img>`** (no wrapper). |
| `.summary-watermark` | Summary slides | Absolutely positioned, 12% opacity, no pointer events |

**🔴 Image rules:** Images must be placed directly — no `<figure>` or wrapper `<div>` around `<img>`. Use `clip-path: inset(...)` for cropping. Apply `border-radius` directly on the `<img>`. Images should use `img://` placeholder syntax; `build-ppt.py --images-dir` handles base64 conversion automatically.
