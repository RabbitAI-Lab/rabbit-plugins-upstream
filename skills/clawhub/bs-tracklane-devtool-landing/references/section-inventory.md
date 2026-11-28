# Section and route inventory

## Home (`data-view="home"`), in order

| # | id | Section | Layout family | Working parts |
| --- | --- | --- | --- | --- |
| 1 | `product` | Hero: one-line h1 (54px), muted 34px subtitle, 2x2 feature notes, Start free + release-note button, "1 of 3" view indicator, scaled product frame | Split, frame top-aligned with the h1, 65px past the container | Indicator bars are the tablist for Board / Cycle / Roadmap (auto-advance one loop with a filling bar, pause on hover/focus/offscreen, arrow keys), live card move with in-app toast |
| 2 | (aria-label Customers) | Wordmark marquee, "Product teams at 2,400 companies..." | Full-width marquee | Pauses on hover; static wrap under reduced motion |
| 3 | `impact` | Two-tone h2 + three metric cards + source footnote | Tall card + two stacked | Count-up once |
| 4 | `workspace` | Bento: triage, threads, backlog health, access, command palette | 12-col bento 7/5 + 5/4/3 | Accept/snooze/decline + empty state + reset, reply, heatmap readout, switches + saved note, command filter + empty state |
| 5 | `cycles` | Mint band: vertical tabs + panel | Tabs + panel | Flows (rule switches), milestones (rebalance + undo), projects, insights (range switch redraws bars) |
| 6 | `workflow` | Copy + steps + integration chips, terminal panel | Split copy / code | CLI / Git / API tabs, copy commands, activity feed lights up once |
| 7 | `evaluate` | Three-step evaluation track + scoping strip | Three cards on a dashed track | Links to security route and demo |
| 8 | `security` | Heading + audit log panel, 2x3 fact grid | Asymmetric split | Link to security route |
| 9 | `customers` | Quote carousel (4 portraits) + customer story card | Portrait + quote, wide card | Prev/next, thumbnails, swipe, arrow keys |
| 10 | `pricing` | Heading + billing switch, three plans, enterprise strip | Plan cards | Monthly/yearly with rolling prices, stored choice |
| 11 | `faq` | Sticky aside + six-item accordion | Aside + accordion | Grid-rows accordion |
| 12 | `start` | CTA card with lanes motif and email form | CTA card | Validation, loading, success, toast |
| - | footer | Brand + newsletter, Product / Company / Trust columns, legal row | Columns | Newsletter form |

## Routes (hash router, JS-held state)

| Route | View | Contents |
| --- | --- | --- |
| `#/` | home | as above |
| `#/pricing` | pricing | Plans with billing switch, grouped comparison table (mobile plan picker), billing FAQ, recommendation strip |
| `#/changelog` | changelog | Filter chips (All, New, Improved, Fixed), search, 9 entries, empty state with Clear filters |
| `#/signin` | signin | Email + password (show/hide), keep signed in, SAML SSO lookup, reset-password pane |
| `#/signup` | signup | Name, work email, workspace name with live address preview, team size, terms; success panel |
| `#/demo` | demo | Benefits, named solutions engineer, demo request form; success panel |
| `#/security` | security | Six security cards, security-pack request form, disclosure contact |
| `#/customers/vantri` | story | Customer story article, facts sidebar, pull quote |
| `#/about` | about | Mission, team photo, numbers, values, open roles accordion with copy email |
| `#/privacy`, `#/terms` | legal | On-page TOC + six sections each |
| anything else | 404 | Lanes motif, "This page took a different lane", links home and to the changelog |

Every view has exactly one h1, which receives focus on route change. Section
anchors (`#workspace`, `#roles`, `#pv-collect`...) switch to the owning view
first, then scroll.

## Data arrays (render functions in the template script)

`ISSUES`, `COLS`, `LABELS`, `PRIO`, `PEOPLE` (board), cycle burn-up series,
roadmap rows, `MARKS` (wordmarks), `TRIAGE`, `HEAT` + `WEEKS`, `CMDS`, `VEL`,
`PLANS`, `CMP`, `CL` (changelog). Rebrand by editing these, not markup.
The route names, plan count (2 to 4), quote count (2 to 5) and the numbers
below are the sample's; replace them with the user's own and keep them in
agreement the same way.

## Numbers that must agree

- Cycle 42 runs Sep 28 to Oct 9; today is Oct 2. Burn-up: scope 58 pts,
  completed 27 (47%), in progress 11, 5 days left. The API example in the
  workflow panel returns the same values.
- PLT-479 (retry with backoff) is the issue in the thread tile, the CLI and Git
  examples and the activity feed; PR #1184 links to it.
- Weekly triage 2 h 10 min to 11 min appears in the metric card and in the
  Vantri quote; 14 teams, 38k issues and -61% carry-over appear on the story
  card and the story route.
- Plans: Free $0 (10 members), Team $10 yearly / $12 monthly, Scale $18 / $22;
  "Save 17%" matches 10 vs 12. The comparison table head reads the same prices.
- 2,400 companies (marquee title, About numbers); 46 people; founded 2021.
