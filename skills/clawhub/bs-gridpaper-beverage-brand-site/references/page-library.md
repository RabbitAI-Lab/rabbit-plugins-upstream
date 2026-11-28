# Page library

The worked example contains 27 routes. Keep the route inventory
and navigation synchronized when adding or removing content.

| Route | Page |
| --- | --- |
| `shop` | Good things come<br>in cartons. |
| `shop/original` | The Original |
| `shop/vanilla` | Vanilla Daydream |
| `shop/cocoa` | Cocoa Club |
| `shop/matcha` | Matcha Moment |
| `shop/berry` | Berry Good |
| `shop/coffee` | Coffee, Please |
| `collections/everyday` | Everyday |
| `collections/sweet-notes` | Sweet notes |
| `collections/tea-coffee` | Tea & coffee |
| `collections/fruit` | Fruit |
| `collections` | Collections |
| `cart` | Your bag |
| `checkout` | Review your order |
| `delivery` | Delivery & care |
| `contact` | Let’s talk |
| `about` | Our story |
| `faq` | Questions, answered |
| `newsletter` | A good thing in your inbox |
| `not-found` | Page not found |
| `recipes/pancakes` | A slow-morning stack |
| `recipes/smoothie` | The pink pick-me-up |
| `recipes/porridge` | A bowl of good intentions |
| `recipes/latte` | Your own little coffee corner |
| `recipes` | Notes & observations |
| `home` | A little oat of the ordinary |
| `stockists` | Find your next carton. |

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
