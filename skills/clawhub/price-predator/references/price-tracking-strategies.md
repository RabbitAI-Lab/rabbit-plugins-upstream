# Price Tracking Strategies

Effective strategies for tracking product prices and timing purchases.

## 1. Establish a Baseline

Before tracking for drops, record at least 2–3 price observations over a few weeks. This establishes a realistic median and helps filter out short-term noise.

```bash
python3 scripts/price_predator.py track --name "Product" --price 400.00 --category electronics
python3 scripts/price_predator.py update <id> --price 395.00
python3 scripts/price_predator.py update <id> --price 389.99
```

## 2. Set a Target Price

Define the price at which you're ready to buy. Price Predator will flag when it's reached.

```bash
python3 scripts/price_predator.py track --name "Product" --price 400.00 --target 300.00 --category electronics
```

## 3. Adjust Alert Sensitivity

The default alert threshold is 10% below median. For high-volatility items, raise it; for stable items, lower it.

```bash
# 15% threshold — only alert on significant drops
python3 scripts/price_predator.py track --name "Product" --price 1000.00 --threshold 0.15
```

## 4. Check Seasonal Timing

Before buying, check whether the current month is a known discount window for the product's category.

```bash
python3 scripts/price_predator.py best-time --category electronics
```

If it says "NOW is a great time to buy," you're in a prime window. If the next window is months away, waiting could save 10–30%.

## 5. Regular Price Checks

Update prices regularly for the best data. Strategies:

- **Manual checks**: Visit the store/website weekly and record the price.
- **Sale events**: Always check during Black Friday, Prime Day, and holiday weekends.
- **Multiple sources**: Use the `--source` flag to tag where each price came from (e.g., amazon, bestbuy, costco).

```bash
python3 scripts/price_predator.py update <id> --price 349.00 --source amazon
python3 scripts/price_predator.py update <id> --price 339.00 --source bestbuy
```

## 6. Read the Sparkline

The ASCII sparkline gives a quick visual of price trend:

```
▁▂▂▃▄▅▅▆▇█
```

- **Upward stairs** (▁▃▅▇): Price rising — buy soon or wait for seasonal dip.
- **Downward stairs** (█▇▅▃▁): Price falling — good sign, may drop further.
- **Flat line** (▄▄▄▄): Price stable — wait for a sale event.
- **Sharp drop** (█▁): Flash sale or clearance — act fast.

## 7. Use the Report for Portfolio Review

Run `report` periodically to review all tracked products at once. It shows:
- Current price vs. median for each product
- Whether any product is near its all-time low
- Whether target prices have been reached
- Recommended best-buy months

## 8. Category-Specific Tips

### Electronics
- New models typically launch in Sep–Oct; previous gen drops immediately.
- Black Friday doorbuster deals may be on lower-quality variants — verify model numbers.

### Mattresses
- Mattress prices are highly negotiable; MSRP is inflated.
- Memorial Day and Labor Day offer the most predictable discounts.

### Appliances
- New appliance models ship in Sep–Oct; last year's models get clearanced.
- Bundle deals during holiday weekends can stack savings.

### Clothing
- Buy at the end of each season for the steepest markdowns.
- January and July are the best clearance months.

## 9. When NOT to Wait

Sometimes buying now is better than waiting for a sale:

- **Limited stock / clearance**: If the item is being discontinued, the current price may be the best you'll get.
- **Urgent need**: If you need it now, the utility of having it outweighs a potential 10% savings months later.
- **Price is already near all-time low**: Check `report` — if it says "Near all-time low," waiting has diminishing returns.

## 10. Database Management

- The default database is at `~/.price_predator_db.json`.
- Use `--db` to maintain separate databases (e.g., personal vs. gift tracking).
- Use `list` to see all tracked products at a glance.
- Use `remove` to clean up products you've purchased or no longer care about.
- Back up the JSON file periodically — it's your price history.
