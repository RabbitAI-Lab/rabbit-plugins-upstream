# Depreciation Tables

> Expected lifespan and annual depreciation rates by category.

These tables are used by `scripts/inventory.py` to calculate current (depreciated) values. Adjust the rates in the script's `DEPRECIATION_RATES` dictionary to match your local market conditions or insurer guidelines.

## How Depreciation Is Calculated

```
current_value = original_value × (1 - annual_rate × years_since_purchase)
```

- Capped at the item's **typical lifespan** — value stops declining after that.
- For appreciating categories (jewelry, art), the formula reverses:
  ```
  current_value = original_value × (1 + appreciation_rate × years_since_purchase)
  ```

## Rate Table

| Category       | Annual Rate | Direction    | Typical Lifespan | Notes                                  |
|----------------|-------------|--------------|------------------|----------------------------------------|
| Electronics    | 25%         | Depreciating | 5 years          | TVs, computers, phones, audio gear     |
| Appliances     | 12%         | Depreciating | 10 years         | Fridge, washer, oven, dishwasher       |
| Furniture      | 8%          | Depreciating | 15 years         | Sofas, tables, beds, shelving          |
| Clothing       | 20%         | Depreciating | 5 years          | Everyday wear; designer may appreciate |
| Tools          | 10%         | Depreciating | 12 years         | Power tools, hand tools, workshop      |
| Sports         | 12%         | Depreciating | 8 years          | Bikes, camping, fitness equipment      |
| Books          | 10%         | Depreciating | 20 years         | First editions/collectible may appreciate |
| Jewelry        | 3%          | **Appreciating** | 100 years    | Gold/diamond values track inflation+   |
| Art            | 5%          | **Appreciating** | 100 years    | Original works, limited prints         |
| Collectibles   | 4%          | **Appreciating** | 100 years    | Coins, stamps, vintage toys            |
| Vehicles       | 15%         | Depreciating | 12 years         | Cars, motorcycles, scooters            |
| Musical        | 6%          | Depreciating | 25 years         | Instruments, audio gear                |
| Other          | 10%         | Depreciating | 10 years         | Default for uncategorized items        |

## Worked Examples

### Electronics — Laptop purchased 3 years ago for $2,000

```
annual_rate = 25%, lifespan = 5 years
years = 3 (under lifespan cap)
current = $2,000 × (1 - 0.25 × 3)
        = $2,000 × 0.25
        = $500
```

### Furniture — Sofa purchased 10 years ago for $1,500

```
annual_rate = 8%, lifespan = 15 years
years = 10 (under lifespan cap)
current = $1,500 × (1 - 0.08 × 10)
        = $1,500 × 0.20
        = $300
```

### Jewelry — Ring purchased 5 years ago for $5,000

```
appreciation_rate = 3% (appreciates)
current = $5,000 × (1 + 0.03 × 5)
        = $5,000 × 1.15
        = $5,750
```

## Adjusting Rates

Open `scripts/inventory.py` and edit the `DEPRECIATION_RATES` dictionary:

```python
DEPRECIATION_RATES = {
    "electronics": (0.25, 5),    # (annual_rate, lifespan_years)
    "furniture":   (0.08, 15),
    "jewelry":     (-0.03, 100), # negative rate = appreciation
    # ...
}
```

### Tips for Adjusting

- **Insurer says different?** Match their depreciation schedule so your reports align.
- **Collector market differs?** For art/collectibles, use real auction results to set appreciation rates.
- **Antiques?** Use the `art` or `collectibles` rate (appreciating) unless you have reason not to.
- **Brand premiums?** Some brands (Apple, Rolex, Hermès) retain value better. Consider a custom category with a lower rate.

## Insurance: ACV vs. Replacement Cost

| Settlement basis        | Which value to use           |
|-------------------------|------------------------------|
| Actual Cash Value (ACV) | Depreciated value            |
| Replacement Cost (RC)   | `estimated_value` (original field) |

Your `insurance-report` shows **both** so you can compare. Most modern policies default to RC — but always verify.
