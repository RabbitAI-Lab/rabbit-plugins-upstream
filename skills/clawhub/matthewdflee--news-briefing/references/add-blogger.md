# Adding New Bloggers

## Quick Method (Conversational)

Users can add a new blogger by simply saying in conversation:

> "Add Finance blogger example_handle"

The AI then automatically performs these three steps:

### Step 1: Update sources.yaml

Add the new blogger under the appropriate category in `config/sources.yaml`:

```yaml
Finance:
  - handle: example_handle
    name: Example Name
    followers: "100K"
```

### Step 2: Update fetch_tweets.py

Add the handle to the `ACCOUNTS` dictionary in `scripts/fetch_tweets.py`:

```python
ACCOUNTS = {
    "Finance": ["existing1", "existing2", "example_handle"],
    # ... other categories
}
```

### Step 3: Update Automation Prompt

Update the automation prompt's account list to include the new handle and update the account count.

## Verification

After adding, test the fetch script:

```bash
python3 scripts/fetch_tweets.py --hours 24 --limit 5 --output data/tweets_raw.json
```

Confirm the new blogger's tweets appear in the output.

## Removing a Blogger

To remove a blogger, reverse the process:
1. Remove from `config/sources.yaml`
2. Remove from `scripts/fetch_tweets.py` ACCOUNTS dictionary
3. Update automation prompt account list and count
