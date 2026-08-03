# Internet Time (Swatch Beats)

Get the current Swatch Internet Time in beats (@000–@999).

## What is Internet Time?

Swatch Internet Time divides the day into 1000 beats. Each beat = 1 minute 26.4 seconds. No time zones, no daylight saving — `@230` means the same moment everywhere on Earth.

Reference: [swatch.com/internet-time](https://www.swatch.com/en-us/internet-time)

## Usage

Ask for the internet time in natural language:

- "What's the internet time?"
- "Current beats?"
- "Swatch time"
- `/beats`

The agent responds with just the beat time: **`@483`**

### Timezone Conversion

You can ask what a beat time means locally:

> "What's @230 in California?"

The agent will convert to the local time for that location.

## Requirements

| Binary | Purpose |
|--------|---------|
| `python3` | Run the beat calculation script |

## How It Works

The script calculates Biel Mean Time (UTC+1, no DST) and divides the day into 1000 equal beats:

1. Get current UTC time
2. Add 1 hour for BMT (UTC+1)
3. Divide total seconds by 86.4 → beat number (0–999)
4. Format as `@` + zero-padded 3 digits

## License

MIT
