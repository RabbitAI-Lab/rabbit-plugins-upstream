---
name: souvenir-sleuth
description: "Find authentic, locally-made souvenirs at any destination and dodge tourist traps. Provides fair local price ranges, where locals actually shop, authenticity tells for handcrafts vs factory fakes, customs/import rules, and trap checks for specific items. Use when the user asks what to buy in a city, whether a souvenir is authentic or a tourist trap, or what gifts they can bring through customs."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [travel, souvenirs, shopping, gifts, authentic, customs, bargaining]
---

# Souvenir Sleuth 🎁

Find **authentic, locally-made souvenirs** at any destination — and dodge the tourist traps. Input a destination (city/region/country), get a ranked catalog of genuinely local gift ideas: what it is, why it's local, the honest price range, where to buy it, and how to verify authenticity (plus customs/shells/food rules that surprise travelers).

## Overview

Travelers face the same disappointment: hours in a "local crafts market" that sells the same mass-produced fridge magnets and made-in-factory "handmade" scarves found at every airport. Meanwhile the actually-local specialties (Lyon's silk, Fez's leather, Oaxaca's alebrijes, Kyoto's yuzen washi) are one street over and cost less.

`souvenir_sleuth.py` builds a destination dossier from a curated knowledge base of **13 destinations** covering:

- signature local crafts/specialties and their cultural origin
- honest local price ranges (souvenir vs. airport vs. tourist-market markup)
- **where** locals actually buy it (named market/street/district types)
- authenticity tells: handcraft marks, regional certifications, fake tells
- what to avoid: common scams, counterfeit-prone items, ethical issues (coral, ivory, endangered wood)
- customs quick-facts for food/plant/leather items (US/AU/EU/UK skews)

The agent layer combines this dossier with live web research to add current shop names, seasonal availability, and packing advice.

## When to Use

- "What should I buy in Lisbon / Kyoto / Marrakech?" — gift ideas with real local cred
- "Is [item] a tourist trap in [city]?" — trap probability + authentic alternative
- "What souvenirs are actually worth buying/can I get through customs?"
- Shopping for gifts for people back home while traveling
- Avoiding counterfeit/illegal souvenirs (ivory, coral, tortoiseshell, certain woods)

**Don't use for:** booking tours/restaurants, currency exchange, or haggling tutoring alone (though the dossier includes fair-price tables useful for haggling).

## Quick Start

```bash
# Dossier for a destination
python3 scripts/souvenir_sleuth.py --destination Kyoto

# Only gifts under a budget (local currency amounts)
python3 scripts/souvenir_sleuth.py --destination "Mexico City" --budget 500

# JSON for the agent to enrich with web research
python3 scripts/souvenir_sleuth.py --destination Fez --json fez.json

# List all destinations in the knowledge base
python3 scripts/souvenir_sleuth.py --list

# Is this item a trap?
python3 scripts/souvenir_sleuth.py --destination Rome --item "Colosseum snow globe"
```

## Workflow (agent)

1. Match the user's destination via the script (aliases handle NOLA, CDMX, Fès, etc.). If not in the offline KB, fall through to live web research using the reference guides' structure.
2. Hand the user the dossier; apply budget/customs filters they mention.
3. Trap-check any specific item they're considering.
4. Enrich top 2-3 picks with web search: current shop names, opening hours, seasonal notes.
5. Check `references/customs-guide.md` for the user's home country before they buy food/leather/plant items.

## Common Pitfalls

1. **"Handmade" at a tourist market ≠ handmade.** Check the authenticity tells in the dossier — e.g., real Fez leather smells vegetal and shows pore grain; "genuine leather" stamped goods from airport shops are usually bonded scraps.
2. **Buying food/plants first, packing last.** Liquids (olive oil, honey >100ml) and fresh produce get confiscated in carry-on; customs facts flag what needs checked luggage or is prohibited outright.
3. **Ignoring haggling culture calibration.** In fixed-price cultures (Japan, much of Europe) haggling insults; in bazaar cultures the sticker price is theater. Each destination card includes a haggling index.
4. **Weight = money.** Ceramics and books are heavy; the dossier lists fragile/heavy warnings so you don't blow your baggage allowance on one bowl.
5. **Confusing "local brand" with "local craft."** A city-themed mug made in China is a memory, not a craft; both are valid — just know which one you're buying.

## Verification Checklist

- [ ] Destination matched the intended city (check aliases)
- [ ] Budget filter applied in the destination's local currency
- [ ] Customs flags reviewed for food/leather/plant items
- [ ] Avoid-list checked for illegal/counterfeit categories before shopping
- [ ] Agent enriched top picks with current shop names/hours via web

## References

- `references/customs-guide.md` — food/plant/leather import rules by traveler home region
- `references/authenticity-tells.md` — how to spot real vs factory "handmade" per material
