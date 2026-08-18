# UI Components

Use the CSS classes provided in the template to create a visually appealing presentation:
- **Typography**: `.slide-label`, `.slide-title`, `.slide-subtitle`, `.em` (blue), `.em-teal`, `.em-red`, `.em-amber`.
- **Layouts**: `.grid-2`, `.grid-3`, `.grid-4` for multiple columns; `.stack-col` for a vertical stack of `.stack-row` layers.
- **Cards**: `.card` (general card), `.feat-card` (feature card with full colored border), `.plat-card` (compact platform card).
- **Color variants**: colored components take a `-blue` / `-teal` / `-red` / `-amber` / `-violet` (or `.b-*` / `.fill-*`) modifier class; always pair them:
  - `.card` + `.b-blue` / `.b-teal` / `.b-red` / `.b-amber` (adds a thick colored top border and colors all list bullet dots inside the card). **IMPORTANT:** Always use these color modifiers on `.card` elements side-by-side in a grid to visually distinguish different key points or topics (e.g., `<div class="card b-blue">`, `<div class="card b-teal">`).
  - `.card` + `.fill-blue` / `.fill-teal` / `.fill-red` / `.fill-amber` / `.fill-violet` (adds a full 2px colored border and a soft wash background). Use this when you want a strongly highlighted, fully colored box.
  - `.feat-card` + `.feat-blue` / `.feat-teal` / `.feat-red` / `.feat-amber` (sets full border and heading color).
  - `.badge` (inside `.card`): automatically inherits the color of the parent card if the card uses a `.b-*` or `.fill-*` modifier. **TIP:** Place the `<span class="badge">` directly inside the `<h3>` (e.g., `<h3><span class="badge">1</span> Title</h3>`) to align the badge and the text perfectly on the same line.
  - `.tag` (standalone label) + `.tag-blue` / `.tag-teal` / `.tag-red` / `.tag-amber`.
  - `.stack-row` + `.stack-blue` / `.stack-teal` / `.stack-red` / `.stack-amber` / `.stack-navy` (for layered architecture diagrams).
- **Images**: `.slide-img` for a single image (contain-fit, max 562px tall); wrap multiple `<img>` in `.img-grid` for an auto-fitting image grid. Always include descriptive `alt` text.
- **Code & Tables**: `.code-block` on a `<pre><code>` for automatic syntax highlighting (via Highlight.js); `.data-table` on a `<table>` (with `<th>` header cells) for data tables; inline `<code>` inside cards, lists, and paragraphs is styled automatically.
- **Diagrams, Charts & Markdown**:
  - **Mermaid.js** (Logical Diagrams): Wrap text diagrams in `<pre class="mermaid">` (e.g. `graph TD`, sequence diagrams, mindmaps). **WARNING**: If you place a Mermaid diagram inside an HTML comment `<!-- ... -->` for any reason, you MUST use thick arrows `==>` or dotted arrows `-.->` instead of thin arrows `-->`. The thin arrow `-->` will prematurely close the HTML comment and break the page layout!
  - **Apache ECharts** (Data Visualizations): Wrap JSON option configuration in `<div class="echarts" data-option='{...}'></div>` or `<pre class="echarts">{...}</pre>` for interactive bar, line, pie, radar, or sankey charts.
  - **Markdown**: Wrap markdown text blocks in elements with `class="markdown"` (rendered by Marked.js).
- **Speaker Notes**: Add `<aside class="notes">Speaker notes content here</aside>` inside any slide. Notes are invisible in the presentation view but displayed in Speaker View.
- **Cover Slide**: Use `.cover-bg`, `.cover-grid`, `.cover-content`, `.cover-logo` (accent word inside `<span>`), `.cover-title` (gradient text via `<span class="h">`), `.cover-divider`, `.cover-sub` (highlight via `<span class="warm">`), and `.cover-stats` with `.cover-stat` items (`.n` = number, `.l` = label) for key metrics.
- **Footers**: Use `.bottom-strip` for key takeaways at the bottom of a slide; inside it, `.em` renders teal and `.wm` renders amber.
- **Animations**: Add `.a` and `.a1` through `.a6` to elements for staggered fade-up animations when the slide becomes active. For inline SVG diagrams, `.flow-anim` / `.flow-anim-slow` animate dashed connector lines and `.pulse-dot` makes a dot pulse.
