# Page library

The template is one HTML file with a hash router. Each page is a
`<section data-page="…" data-title="…">` inside `<main>`; the header and
footer are shared. Routes: `#/` (home), `#/about`, `#/work`,
`#/work/<slug>` (eight detail pages), `#/services`, `#/contact`, and
`not-found` for anything else. All fourteen ship by default.

## Shared chrome

- **Header** (`.top`, sticky, blurred ground): wordmark with a small
  uppercase discipline label, five text links with an underline that
  scales in on hover and on the active route, and a dark "Start a
  project" button. Under 900px the links collapse behind a bordered
  square toggle (`i-menu` / `i-x`) into a dropdown panel.
- **Footer** (`.footer`, four columns): wordmark and blurb; Pages;
  Recent work (four projects plus "All projects"); Contact lines. Bottom
  row: copyright line and a back-to-top text button.

## Home (`home`) — canonical order

1. **Hero** (`.hero`): portrait cut-out left, bottom-aligned; right column
   with the staggered display title, name, discipline, three meta chips
   and two buttons (primary to Work, ghost to Contact).
2. **About teaser + toolkit** (`.about-grid`): "About me" chip and a bio
   paragraph with bolded facts and a "More about me" link; beside it the
   "Toolkit" chip and four tool tiles.
3. **Poster grid** (`.poster-grid`): centred "My projects" chip, eight
   poster cards linking to their detail pages, "All projects" ghost
   button.
4. **Service rows** (`.svc-rows`): "Services" chip with a one-line intro
   and four numbered hairline rows linking to Services.
5. **CTA band** (`.cta-band`): headline, one sentence, primary and ghost
   buttons.

## About (`about`)

1. Page head: "About" chip, headline, lead.
2. `.about-cols`: tilted white photo frame with a mono caption; three bio
   paragraphs and a four-cell facts list.
3. "Path" chip and a timeline of dated rows (year, role and organisation,
   one line).
4. `.two-col`: extended toolkit tiles; "How I work" check list.
5. "What I care about" chip and three value cards with icon boxes.
6. CTA band.

## Work (`work`)

1. Page head: "Selected work" chip, headline, lead.
2. Filter chips (`data-filter-group`) for All, Event, Print,
   Illustration, Packaging, Music; each poster card carries `data-cat`.
3. The same eight poster cards as Home.
4. A hairline note row with a "Request the full archive" link.

## Poster detail (`work/<slug>`, eight pages)

`.case-grid`: sticky poster figure on the left; on the right: breadcrumb
(Work / Title), title, one-line summary, meta list (Client, Year,
Category, Role), Brief, Approach (two paragraphs), Outcome, Deliverables
(four items with `i-check`), Palette (three or four hex swatches), and
`.case-nav` with previous and next links that chain all eight in a loop.

Demo slugs: `harbor-lights`, `kestrel-roast`, `lantern-fox`,
`field-notes-riso`, `typewriter-bloom`, `chrome-loop`, `adoption-day`,
`ridge-run`.

### Adding a project

1. Duplicate one detail section, change `data-page`, `data-title`, the
   image, and every text slot.
2. Add a poster card to both grids (Home and Work) with the next index
   number and a matching `data-cat`; add a filter chip if the category is
   new.
3. Re-point the previous/next links of the neighbouring projects.
4. Optionally list it under "Recent work" in the footer.
5. Run the validator; it fails on any link that has no section.

## Services (`services`)

1. Page head: "Services" chip, headline, lead.
2. `.svc-list`: four translucent cards, each with a number, title,
   summary, four includes with check icons, a "From $…" price with a
   turnaround line, and a "Request this" button to Contact.
3. "Process" chip and four hairline-topped steps.
4. `.two-col`: "Questions" chip and intro; plus accordion with four
   items (`data-accordion`).
5. CTA band.

## Contact (`contact`)

1. Page head: "Contact" chip, headline, lead.
2. `.contact-grid`: two-column demo form (name, email, project type,
   budget, date, message, submit with `i-send`, reassurance line) that
   shows an in-page confirmation and never submits; dark contact card with
   email, phone, studio and availability rows plus handle chips.

## Not found (`not-found`)

Centred "404" chip, "Nothing here." headline, one sentence, buttons home
and to Work. Reached by any unknown hash.
