# Page library

The worked example contains 14 routes. Keep the route inventory
and navigation synchronized when adding or removing content.

| Route | Page |
| --- | --- |
| `home` | Home |
| `about` | About |
| `work` | Work |
| `work/harbor-lights` | Harbor Lights |
| `work/kestrel-roast` | Kestrel Roast |
| `work/lantern-fox` | Lantern Fox |
| `work/field-notes-riso` | Field Notes |
| `work/typewriter-bloom` | Typewriter Bloom |
| `work/chrome-loop` | Chrome Loop |
| `work/adoption-day` | Adoption Day |
| `work/ridge-run` | Ridge Run |
| `services` | Services |
| `contact` | Contact |
| `not-found` | Page not found |

## Content requirements

A detail page needs a specific introduction, its own image subject, useful
body sections and a route back to the collection. Product pages include
price and option selection; journeys include itinerary and booking context;
case studies explain the brief, response and delivered work; articles need
a complete narrative rather than a card description repeated as body text.

## Adding a page

Create the page, add a collection card and a navigation or contextual link,
then test the route directly and through its visible entry point. In the
catalog demo use a unique data-page and hash route. In the generated website
use actual routes in the selected framework. See framework-adaptation.md.

## Shared interaction contract

- Menus: open, close, keyboard focus and close after route navigation.
- Collections: search, category selection, sorting and no-results state.
- Commerce where present: item options, add, quantity, remove, totals and
  disabled empty checkout. A real integration must implement backend checks.
- Forms: required fields, clear feedback and no false delivery claims.
- Tabs and carousels: a visible selected state and a real content change.
- Links: each visible action resolves to its named destination.
