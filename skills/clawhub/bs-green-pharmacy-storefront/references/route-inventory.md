# Page library

The worked example contains 34 routes. Keep the route inventory
and navigation synchronized when adding or removing content.

| Route | Page |
| --- | --- |
| `home` | Home |
| `catalog` | Catalog |
| `product/sunlift-vitamin-d3` | Sunlift Vitamin D3 |
| `product/honeybark-cough-syrup` | Honeybark Cough Syrup |
| `product/omega-3-deep-sea` | Omega-3 Deep Sea |
| `product/clearmist-eye-drops` | ClearMist Eye Drops |
| `product/aloe-fresh-sanitizer` | Aloe Fresh Sanitizer |
| `product/rapidease-ibuprofen` | RapidEase Ibuprofen |
| `product/plant-protein-vanilla` | Plant Protein Vanilla |
| `product/saline-nasal-mist` | Saline Nasal Mist |
| `product/ceramide-repair-cream` | Ceramide Repair Cream |
| `product/home-first-aid-kit` | Home First-Aid Kit |
| `product/digital-thermometer` | Digital Thermometer |
| `product/electrolyte-sachets` | Electrolyte Sachets |
| `product/stage-2-infant-formula` | Stage 2 Infant Formula |
| `product/mango-pear-puree` | Mango & Pear Puree |
| `product/oat-banana-baby-cereal` | Oat & Banana Cereal |
| `product/overnight-diapers-size-4` | Overnight Diapers |
| `product/sensitive-water-wipes` | Sensitive Water Wipes |
| `product/gentle-baby-lotion` | Gentle Baby Lotion |
| `product/honey-wheat-clusters` | Honey Wheat Clusters |
| `cart` | Cart |
| `checkout` | Checkout |
| `consultation` | Consultation |
| `prescriptions` | Prescriptions |
| `brands` | Brands |
| `faq` | FAQ |
| `about` | About |
| `contact` | Contact |
| `account` | Account |
| `app` | App |
| `privacy` | Privacy |
| `terms` | Terms |
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
