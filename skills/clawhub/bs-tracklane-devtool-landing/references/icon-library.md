# Icon library

Every icon is inline SVG. Emoji, Unicode dingbats (check marks, arrows, stars,
sparkles, bullets, the command-key glyph) and icon fonts are defects.

## Lucide sprite (general UI)

The template defines `<symbol>`s once at the top of `<body>` and uses
`<svg class="icon"><use href="#i-name"/></svg>`. Grammar: 24 viewBox,
`fill="none"`, `stroke="currentColor"`, stroke-width 1.75, round caps and
joins. In React use `lucide-react` with the same names.

| Slot | Symbol (Lucide name) |
| --- | --- |
| CTA and link arrows | `i-arrow-right` (ArrowRight), `i-arrow-left` |
| Dropdown, breadcrumbs | `i-chevron-down`, `i-chevron-right` |
| Plan features, comparison, success | `i-check`, `i-minus`, `i-circle-check` |
| Product menu | `i-kanban`, `i-inbox`, `i-refresh` (RefreshCw for cycles), `i-blend`, `i-git-branch`, `i-shield` (ShieldCheck) |
| Cycles tabs | `i-circle-dot`, `i-diamond`, `i-blend`, `i-chart` (ChartNoAxesColumn) |
| Metric cards | `i-zap`, `i-circle-check`, `i-flag` |
| Developer workflow | `i-git-branch`, `i-git-pr` (GitPullRequest), `i-git-merge`, `i-terminal`, `i-copy` |
| Integrations by category | `i-workflow` (CI), `i-message` (chat), `i-siren` (alerts), `i-life-buoy` (support), `i-pen` (design) |
| Security | `i-shield`, `i-key` (KeyRound), `i-file-text`, `i-globe`, `i-lock`, `i-users`, `i-server`, `i-target`, `i-bell` |
| Forms and auth | `i-mail`, `i-eye`, `i-eye-off`, `i-alert` (TriangleAlert), `i-calendar` |
| Chrome | `i-menu`, `i-x`, `i-search`, `i-command`, `i-sun`, `i-moon`, `i-rss` |
| Roles and meta | `i-map-pin`, `i-briefcase`, `i-clock`, `i-users` |

Swap-in candidates that stay on style: `ListChecks`, `Timer`, `Gauge`,
`Workflow`, `Webhook`, `Bug`, `Rocket`, `CalendarClock`, `Filter`.

## Product glyphs (14 viewBox, part of the product UI)

- Status: `st-backlog` (dashed ring), `st-todo` (ring), `st-progress` (ring +
  half pie), `st-review` (ring + three-quarter pie), `st-done` (filled circle +
  check). Color them with the `--st-*` tokens.
- Priority: `pr-urgent` (filled square with exclamation stroke), `pr-high`,
  `pr-med`, `pr-low` (three bars with 1 to 3 filled). Give them `role="img"`
  and an `aria-label` such as "High priority".

## Fictional customer marks

Simple geometric marks (`m-halcyra` rising arcs, `m-vantri` triangle,
`m-orrelby` ring, `m-kestova` rotated square, `m-pellmar` twin pills, `m-druvo`
quarter block, `m-sennet` three dots, `m-ilvara` asterisk) beside a typeset
wordmark, each wordmark in a different weight or case. Single color
(`currentColor`), so they work in both themes. Never draw or imitate a real
company's logo; integrations are named by category, not by brand.

## Brand mark

Ink rounded square (rx 7.5 on 26) with three lanes of different length in the
ground color and a lane-green dot at the end of the middle lane. The favicon is
the same mark as an SVG data URI.
