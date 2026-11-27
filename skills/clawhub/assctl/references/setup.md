# Setup

Install with Go 1.26 or newer.

```bash
go install github.com/psyb0t/assctl/cmd/assctl@latest
assctl version
assctl fonts-install
```

## Named looks

- `black-gold` uses a black background, white text, and gold as its secondary karaoke color.
- `ivory-navy` uses a navy background, ivory text, and sky blue as its secondary karaoke color.
- `mint-plum` uses a plum background, mint text, and peach as its secondary karaoke color.
- `clean` uses an outline on a clear background.
- `tiktok-bold` uses TikTok Sans Bold for lower-middle speech captions.
- `reels-bold` uses Barlow Condensed ExtraBold for lower-middle speech captions.
- `shorts-impact` uses yellow Anton text with a black outline.
- `social-center` centers white Anton text; `social-hook` puts yellow Barlow Condensed ExtraBold near the top.
- `social-box` uses TikTok Sans Bold on translucent black.
- `the-bold` uses the free version of THE BOLD FONT, downloaded from the author's DaFont page. Use uppercase text.

Run `assctl presets --json` for complete parameters. Existing inline tags remain intact and take precedence over the style definition.

Social presets scale their horizontal margins with the script width and their vertical margins with its height. Supply the intended video dimensions. Keep phrases short and check the result against the destination app's controls. Font download links, terms, and position details are in the [preset guide](https://psyb0t.github.io/assctl/presets/).

## Precise edits

Inspect a document first. Its JSON output shows the exact field names. Supply an edit spec with `Info`, `Styles`, or `Events`. An event index starts at one. Use typed `Override` fields to add tags without replacing dialogue text.

```json
{
  "Styles": [
    {
      "Name": "Default",
      "Fields": {
        "Fontsize": "52"
      }
    }
  ]
}
```

```bash
assctl edit --spec edits.json --output updated.ass captions.ass
```

See the [CLI guide](https://github.com/psyb0t/assctl/blob/main/docs/cli.md) for the full creation and editing examples.

## Independent placement and tags

Use `assctl positions --json` to list `portrait-upper`, `portrait-center`, and `portrait-lower-middle`. `--text-position NAME` works with `create`, `captions`, and `theme`. For a placement-only edit, use `assctl position INPUT --text-position NAME --output FILE`; `--style NAME` limits it to one style. These layouts use script coordinates and cannot guarantee clearance from every app's controls.

`assctl tags --spec override.json` prints an ASS override block. The JSON shape is `ass.Override`, also accepted by event creation and edits. See [ASS features](https://psyb0t.github.io/assctl/ass-features/) for drawing, karaoke, clipping, wrapping, and validation boundaries.
