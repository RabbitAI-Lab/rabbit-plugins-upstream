# Page library

The worked example contains 19 routes. Keep the route inventory
and navigation synchronized when adding or removing content.

| Route | Page |
| --- | --- |
| `home` | Home |
| `work` | Work |
| `work/pine-and-pepper` | Pine and Pepper |
| `work/lantern-tea` | Lantern Tea Co. |
| `work/bumble-crayons` | Bumble Crayons |
| `work/marrow-bay-surf` | Marrow Bay Surf |
| `services` | Services |
| `services/identity-systems` | Identity systems |
| `services/brand-strategy` | Brand strategy |
| `services/packaging-design` | Packaging design |
| `services/collateral-campaigns` | Collateral and campaigns |
| `about` | About |
| `insights` | Insights |
| `insights/brand-personality` | Brand personality |
| `insights/more-than-a-logo` | More than a pretty logo |
| `insights/consistency-builds-trust` | Consistency builds trust |
| `process` | Process |
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
