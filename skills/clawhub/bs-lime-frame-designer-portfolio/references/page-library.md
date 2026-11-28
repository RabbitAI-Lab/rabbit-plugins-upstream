# Page library

Every page is a `<section data-page="…" data-title="…">` inside `<main>`.
Routes are hashes: `#/` is `home`, `#/services/brand-identity` is
`services/brand-identity`. Unknown routes fall back to the top segment,
then to `not-found`.

## Pages that always ship (18 in the example)

| Route | Page | Purpose |
| --- | --- | --- |
| `#/` | home | the full landing story |
| `#/about` | about | bio, principles, career path, toolkit |
| `#/services` | services | four service cards, process, CTA |
| `#/services/<slug>` | 4 service pages | includes, steps, related work, price aside |
| `#/work` | work | filter chips and six cards |
| `#/work/<slug>` | 6 case pages | brief, approach, outcome, results, deliverables, next |
| `#/testimonials` | testimonials | six quote cards and a survey stats band |
| `#/faq` | faq | eight-item accordion with a contact aside |
| `#/contact` | contact | contact card, brief form, three tips |
| any other | not-found | 404 number, one line, home button |

## Home, canonical order

1. **Header**: wordmark with a black disc, centred links, black pill CTA
   with a lime arrow disc; hamburger and dropdown under 960px.
2. **Hero** (`.hero`): left greeting, uppercase name, intro, lime pill;
   centre portrait card with social column and availability line; right
   award line with a left rule, two-tone role, avatar stack with a badge,
   proof number and tagline.
3. **Wordmark row** (`.clients`): "Trusted by" label and the marquee.
4. **Services preview**: eyebrow, title, "All services" link, four cards
   with numbered lime icon discs.
5. **Collaboration split** (`.collab`): two-tone headline, phone and email
   items, black pill; two mockup shots.
6. **Stats band** (`.band`): two-tone headline, studio thumbnail with play
   disc, three count-up numbers.
7. **Selected work**: three featured work cards.
8. **Testimonials preview**: three cards, the middle one lime-tinted.
9. **FAQ preview**: three accordion items and an "All questions" link.
10. **CTA band** (`.cta`): lime panel, headline, one line, black pill.
11. **Footer**: brand and blurb, Pages, Services, Contact columns; bar
    with copyright and four circular social buttons.

## Section anatomy

- **Page hero** (`.page-hero`): optional breadcrumbs, eyebrow, big title,
  lead paragraph; case pages add a four-column meta strip.
- **Service page** (`.detail`): prose with "What's included" check list,
  three process steps, two related work cards; sticky aside with price,
  a definition list and a lime pill.
- **Case page**: 16:8 hero image, prose with three headed paragraphs,
  three lime result tiles; sticky deliverables aside; "next project" row
  that chains the six cases into a loop.
- **About**: sticky portrait card beside three-paragraph prose and three
  fact tiles; three value tiles; timeline rows; skill chips; CTA.
- **Testimonials**: `.tcard` with five stars, quote, initials avatar,
  name and role, and a "Read the case study" link.
- **Contact**: `.contact-card` on `--panel` with four contact rows and
  hours; a two-column brief form with in-page confirmation.

## Extending

- **Add a service**: copy a `services/…` section, add a card on the
  services page and in the home preview grid, add a footer link.
- **Add a project**: copy a `work/…` section, give it a slug, add a card
  with a `data-cat` value to the work grid, feature it on home if wanted,
  and update the previous case's "next project" link.
- **Remove a page**: delete its section and every link to it; the
  validator reports any link that no longer resolves.
