## Description:

Market Heatmap renders a self-contained interactive HTML treemap of U.S. stock indices, sized by market cap and colored by price move or available SentiSense overlays, using one read-only SentiSense API request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market analysts use this skill to generate a static U.S. market heatmap for sector performance, movers, market mood, sentiment, score, mentions, and options-interest views. The output is a delayed research snapshot, not trading advice, a recommendation, or a forecast.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and makes an HTTPS request to SentiSense.

Mitigation: Provide the key through the SENTISENSE_API_KEY environment variable, install only if the SentiSense request is acceptable, and avoid pasting the key into prompts or generated output.

Risk: The generated market board can be mistaken for live data, trading advice, a recommendation, or a forecast.

Mitigation: Present the board as a delayed research snapshot, preserve as-of labels, and do not use it as the basis for account, trading, purchase, or wallet actions.

Risk: The skill writes local HTML and optional JSON output files.

Mitigation: Write outputs to a controlled path and review before sharing; evidence says the generated HTML contains no API key and performs no runtime network calls.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)
- [SentiSense Market Heatmap Endpoint](https://app.sentisense.ai/api/v1/trackers/market-heatmap?scope=sp500)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/market-heatmap)
- [SentiSense Pricing](https://app.sentisense.ai/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, HTML file, JSON file, guidance]

**Output Format:** [Markdown summary with shell commands, plus a self-contained HTML heatmap and optional JSON summary sidecar]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; makes one read-only HTTPS request per render; generated HTML is a static snapshot with no embedded API key or runtime network calls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
