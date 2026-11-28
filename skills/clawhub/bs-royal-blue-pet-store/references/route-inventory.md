# Page library

The worked example contains 29 routes. Keep the route inventory
and navigation synchronized when adding or removing content.

| Route | Page |
| --- | --- |
| `catalog` | For their everyday. |
| `catalog/daily-bowl` | Daily Bowl |
| `catalog/harbor-lead` | Harbor Lead |
| `catalog/play-rope` | Play Rope |
| `catalog/cloud-bed` | Cloud Bed |
| `catalog/gentle-wash` | Gentle Wash |
| `catalog/weekender` | Weekender Carrier |
| `catalog/soft-harness` | Soft Harness |
| `catalog/puzzle-ball` | Puzzle Ball |
| `categories/food` | Food |
| `categories/accessories` | Accessories |
| `categories/toys` | Toys |
| `categories/beds` | Beds |
| `categories/care` | Care |
| `categories/travel` | Travel |
| `categories` | Categories |
| `contact` | Let’s talk |
| `about` | Our story |
| `faq` | Questions, answered |
| `newsletter` | A good thing in your inbox |
| `not-found` | Page not found |
| `cart` | Your bag |
| `checkout` | Review your order |
| `delivery` | Delivery & care |
| `care-guide/bath-day` | A calmer bath day |
| `care-guide/quiet-corner` | A corner of their own |
| `care-guide/daily-walk` | The good in an everyday walk |
| `care-guide` | Notes & observations |
| `home` | A good life together |

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
