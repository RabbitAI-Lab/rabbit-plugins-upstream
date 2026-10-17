## Description:

Compare US housing markets by city, metro, county, or ZIP code using Crawlora's historical housing dataset and optional live Redfin context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and homebuyers compare US housing markets across matched regions, property types, and periods to understand prices, inventory, sales activity, time on market, and qualified affordability trends.

### Deployment Geography for Use:

Global (analysis covers US housing markets only)

## Known Risks and Mitigations:

Risk: Housing search locations, filters, or sensitive details may be sent to Crawlora/Redfin-backed services along with an API key.

Mitigation: Use a dedicated API key and avoid secrets, private client data, and sensitive personal details in queries.

Risk: Different measurement windows, sparse transactions, or mixed live and historical sources can make market comparisons misleading.

Mitigation: Match periods and property types, label source and measurement windows, and preserve missing values and low-count caveats.

Risk: Modeled affordability can be mistaken for a personal mortgage qualification or financial recommendation.

Mitigation: Disclose income vintage and financing assumptions; keep modeled comparisons separate from individual financial decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/housing-market-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Housing market endpoint reference](reference/endpoints.md)
- [Redfin data center and methodology](https://www.redfin.com/news/data-center/)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison tables and narrative, with optional time-series charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels geography, property type, measurement window, units, activity counts, sources, collection time, and missing data.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
