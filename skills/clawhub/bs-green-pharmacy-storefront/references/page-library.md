# Page library

Every page is a `<section data-page="…">` inside `<main>`. The router shows
exactly one at a time. Query strings after the route (`#/catalog?cat=baby`)
are parsed by the router and passed to the page.

## Pages that always ship

| Route | data-page | Purpose |
| --- | --- | --- |
| `#/` | `home` | the long storefront page (anatomy below) |
| `#/catalog` | `catalog` | every product with filter chips, sort select, search and an empty state |
| `#/product/<id>` | `product/<id>` | one real detail page per product |
| `#/cart` | `cart` | in-memory cart with quantity steppers, remove, promo code, totals |
| `#/checkout` | `checkout` | demo delivery form with order summary and confirmation state |
| `#/consultation` | `consultation` | four steps, booking form with slots, pharmacist roster |
| `#/prescriptions` | `prescriptions` | upload form (file name only, nothing sent), how it works, repeats |
| `#/brands` | `brands` | brand cards linking to `#/catalog?brand=<id>` |
| `#/faq` | `faq` | grouped accordions |
| `#/about` | `about` | stats, portrait split, three values |
| `#/contact` | `contact` | three contact cards, form, opening hours |
| `#/account` | `account` | demo sign-in and health-card membership |
| `#/app` | `app` | app features and the store chips |
| `#/privacy`, `#/terms` | `privacy`, `terms` | short legal pages |
| any unknown | `not-found` | friendly 404 with links home and to the catalog |

The demo ships 19 product pages; a real store can carry as many as needed.
Every link in the header, footer, cards, promo tiles and breadcrumbs must
land on one of these pages. No `href="#"`.

## Home anatomy (canonical order)

1. **Header** – brand, delivery location, search, pharmacy-services pill,
   Offers, Cart with count badge, Sign in; second row of nav pills. Below
   860px the search hides, a hamburger opens the nav as a vertical list with
   the pills in a wrapping CTA row.
2. **Hero frame** – display word, uppercase copy, two badges, portrait, upload
   card, navy CTA.
3. **Category tiles** – six square pastel photos with labels; each links to a
   catalog filter.
4. **Today's best deals** – section head with "See all products" link, four
   discounted product cards.
5. **Service duo** – yellow prescription-upload card, peach consultation card.
6. **Featured brands** – seven monogram discs, "See all" to the brands page.
7. **Trending products** – tab chips (All + six categories) over an eight-card
   grid; tabs filter in place.
8. **Promo tiles** – three pastel tiles with masked figures and an offer.
9. **Baby food collection** – four baby product cards.
10. **Feature banner** – aqua cereal (or any hero product) frame with flavour
    bars.
11. **Testimonials** – rating summary, four quote cards with monogram avatars.
12. **Perk duo** – yellow free-delivery card with courier photo, lime
    health-card tile with a CSS card stack.
13. **Got questions?** – six-item accordion, one open by default.
14. **App duo** – grey card with a fanned stat-card cluster and store chips;
    yellow card with a CSS phone mockup.
15. **Footer** – five columns, social icon row, lime wordmark band, legal line.

## Inner page anatomy

- Every inner page opens with a `.phead` pastel frame (title, one-sentence
  lede, optional right-side chip or button). Rotate pastels between adjacent
  pages: catalog lime, cart mint, checkout yellow, consultation peach,
  prescriptions yellow, brands sky, FAQ lilac, about lime, contact mint.
- Forms use `.form-card` with a two-column `.form-grid`, `.radio-row` pills
  and a `.form-ok` confirmation that appears on submit. Forms never send.
- A `.side-card` beside the form carries the reassurance list.

## Product detail page anatomy

1. Breadcrumb: Home > Catalog > Category > Product.
2. Two columns: grey image well with the sale badge; category chip + rating,
   name, brand line with the verified icon, blurb, price with save chip,
   three benefit rows, quantity stepper + navy Add to cart + lime Go to cart,
   three perk facts.
3. Body: "About this product" and "How to use" prose left; "Details" grey
   panel with a four-row definition list right, plus a safety note linking to
   consultation.
4. "You may also like": four cards from the same category, topped up with
   the highest-rated products from elsewhere.

### Adding a product

Add one `.pcard` (with `data-id`, `data-cat`, `data-brand`, `data-price`,
`data-rating`, `data-deal`, `data-name`) to the catalog grid and to any home
row it belongs in, one `<section data-page="product/<id>">` following the
anatomy above, and one entry in the `PRODUCTS` array at the top of the
script (id, name, price, img, tag) so the cart can price it. In the demo
source these are generated from one data array; keep that approach if you
extend the generator.

## Widgets in the engine

- Router with query parsing, active nav, title update, scroll-to-top,
  reveal re-observe, menu close.
- Cart: `Map` in memory only; header badge; cart and checkout render from
  the same totals (5% member discount, promo `WELCOME5`, $4.90 delivery
  under $35 unless member). Checkout submit clears the cart.
- Catalog: filter chips, brand filter from the query, search from the header
  box, sort select (featured, price both ways, rating), empty state, count.
- Trending tabs, FAQ accordions (one open per group), consultation slot
  chips, quantity steppers, upload file-name echo, toast.
