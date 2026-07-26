# Information Source Configuration

## sources.yaml Format

```yaml
ICT Trading:
  - handle: example_trader1
    name: Example Trader 1
    followers: "100K"

US Stocks:
  - handle: example_trader2
    name: Example Trader 2
    followers: "200K"

AI:
  - handle: example_ai1
    name: Example AI Researcher
    followers: "150K"

Politics:
  - handle: example_politician
    name: Example Politician
    followers: "50M"

Finance:
  - handle: example_finance
    name: Example Finance Account
    followers: "180K"

Tech:
  - handle: example_tech
    name: Example Tech Leader
    followers: "60M"
```

## Category Guidelines

| Category | Focus | Example Topics |
|----------|-------|----------------|
| ICT Trading | Smart Money Concepts, Inner Circle Trader | Trading setups, market structure |
| US Stocks | Stock market analysis | ES futures, stock picks, market commentary |
| AI | Artificial intelligence | New models, research, industry trends |
| Politics | Political figures | Policy changes, geopolitical events |
| Finance | Financial commentary | Macro economics, market analysis |
| Tech | Technology leaders | Product launches, industry vision |

## Adding a New Category

1. Add a new top-level key in `sources.yaml`
2. Add the category name to the automation prompt's account list
3. Add the category to `scripts/fetch_tweets.py` ACCOUNTS dictionary
4. Use the category name in briefing format (translate to Chinese if preferred)
