# Weather & Activity Logic Reference

This document explains the selection rules that `packing_pro.py` uses to build a packing list.

## 1. Season / Temperature Rules

The script first determines the climate category from season and optional temperature override:

| Condition | Climate Category |
|---|---|
| temp ≤ 0°C | `freezing` |
| 0°C < temp ≤ 10°C | `cold` |
| 10°C < temp ≤ 20°C | `mild` |
| 20°C < temp ≤ 30°C | `warm` |
| temp > 30°C | `hot` |

If `--temp-c` is not provided, the season determines the default:

| Season | Default Temp Range | Climate |
|---|---|---|
| winter | -5 to 5°C | cold / freezing |
| spring | 10 to 18°C | mild |
| autumn | 8 to 16°C | mild |
| summer | 22 to 32°C | warm / hot |

### Climate → Clothing Selection

**Freezing / Cold** (≤ 10°C):
- Thermal base layer (top + bottom) — quantity scales with duration
- Heavy sweater or fleece
- Winter coat or down jacket
- Warm hat (beanie), gloves, scarf
- Thermal socks
- Warm sleepwear

**Mild** (10–20°C):
- Long-sleeve shirts
- Light jacket or hoodie
- Mix of jeans and lighter trousers
- Light scarf (optional)

**Warm / Hot** (> 20°C):
- T-shirts and shorts
- Light, breathable fabrics
- Sunglasses, sun hat
- Swimwear if activity includes beach/swimming
- Light sleepwear

### Season-Specific Extras

| Season | Extra Items |
|---|---|
| summer | Sunscreen SPF 50+, sunglasses, sun hat, insect repellent |
| winter | Lip balm, moisturizer, hand warmers |
| spring | Light rain jacket, allergy medication |
| autumn | Light rain jacket, layers |

## 2. Activity Rules

Activities are specified with `--activities` (space-separated). Each adds specialized gear:

### `hiking`
- Hiking boots
- Daypack
- Water bottle
- Trail map / GPS
- First aid kit
- Moisture-wicking base layer

### `swimming` / `beach`
- Swimwear (×2)
- Beach towel
- Sunscreen (already in summer, but always added for beach)
- Waterproof phone case
- Flip-flops / sandals

### `business`
- Laptop + charger
- Business cards
- Notebook + pen
- Dress shirt / blouse
- Dress shoes
- Blazer or suit (if `formal` also specified)

### `skiing` / `snow`
- Ski gloves
- Ski goggles
- Neck gaiter / balaclava
- Hand warmers
- Full thermal base layer
- Ski jacket / pants (or note: rent at destination)

### `photography`
- Camera body
- Extra batteries
- Memory cards
- Cleaning kit
- Tripod (optional — flagged)

### `formal`
- Suit / evening dress
- Dress shoes
- Tie / bow tie
- Cufflinks / accessories

### `camping`
- Tent (or note: check if provided)
- Sleeping bag
- Headlamp / flashlight
- Multi-tool
| Fire starter / matches
| Insect repellent

## 3. Transport Rules

### `flight`
- Liquid restriction note: containers ≤ 100 ml in carry-on
- Universal power adapter (international)
- Travel pillow
- Noise-cancelling headphones recommended
- Passport check (international)
- All chargers in carry-on

### `train`
- Smaller bag (overhead storage)
- Entertainment (book, downloaded movies)
- Snacks
- Travel pillow

### `car`
- Driver's license + registration
- Phone mount / car charger
- Roadside emergency kit
- Cooler / snacks
- Sunglasses (driving)
- Music playlist / podcasts downloaded

### `bus`
- Compact bag (under-seat storage)
- Valuables on person (not in cargo hold)
- Entertainment
- Snacks
- Motion sickness medication

## 4. Duration Scaling Rules

Clothing quantities scale with trip duration:

| Item Type | Formula |
|---|---|
| Underwear | duration + 1 |
| Socks | duration + 1 |
| T-shirts / shirts | ceil(duration / 2) + 1, max 8 |
| Trousers / jeans | ceil(duration / 3), min 1, max 4 |
| Outer layer (jacket/coat) | 1 (wear on travel day) |
| Pajamas | 1 (2 if duration > 7) |

**Laundry buffer**: If duration > 7 days, reduce clothing to max quantities and add a note: "Plan a laundry day around day 5–6."

## 5. Critical Items Logic

The following are **always** included in `critical_items` regardless of other inputs:

- Passport / ID (with expiry check note for international)
- Phone + charger
- Prescription medications (note: in original containers)
- Credit/debit cards + emergency cash
- Travel insurance documents
- Emergency contact list

Transport-specific additions to critical items:
- **flight**: Boarding pass / e-ticket
- **car**: Driver's license + vehicle registration
- **international**: Visa (if required), universal adapter
