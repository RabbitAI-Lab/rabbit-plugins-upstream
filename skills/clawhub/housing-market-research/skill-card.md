## Description:

Compare US housing markets through Crawlora's historical housing dataset and Redfin tools for city, metro, county, or ZIP-code comparisons of prices, inventory, sales activity, time on market, and qualified affordability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to compare defined US housing markets over comparable periods using Crawlora's housing-market dataset and optional Redfin context. It supports market-level research tables and time-series summaries while keeping aggregate trends separate from individual property valuation or financing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housing-market search parameters and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the key scoped to Crawlora, store it in the environment, rotate it if exposed, and review Crawlora's terms before using live Redfin context.

Risk: Market aggregates may be mistaken for individual property valuation, fixed-home appreciation, or personal mortgage qualification.

Mitigation: Label geography, property type, measurement window, assumptions, source, collection time, and missing data; keep individual financing scenarios separate from returned market data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Redfin source and methodology](https://www.redfin.com/news/data-center/)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/housing-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with comparison tables, optional chart guidance, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include region, property type, measurement window, units, sample/activity counts, source, collection time, and missing-data notes.]

## Skill Version(s):

1.0.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
