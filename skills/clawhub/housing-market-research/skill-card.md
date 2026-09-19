## Description:

Compare US housing markets through Crawlora's historical housing dataset and Redfin tools. Use for city, metro, county, or ZIP-code comparisons of prices, inventory, sales activity, time on market, and explicitly qualified affordability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare US city, metro, county, ZIP-code, or national housing-market aggregates over comparable periods. It helps produce market comparison tables, optional time-series views, and qualified affordability interpretation without treating aggregates as individual property valuations or personalized financing advice.

### Deployment Geography for Use:

Global use; data scope is United States housing markets.

## Known Risks and Mitigations:

Risk: The skill sends the user's housing-market query parameters and Crawlora API key to Crawlora's API.

Mitigation: Install only when that data sharing is acceptable, keep the API key in the environment, and avoid placing secrets in prompts, files, or command-line arguments.

Risk: Affordability outputs can be mistaken for personalized financial advice or mortgage qualification.

Mitigation: Present affordability as a market-level estimate and disclose the income vintage, income geography, mortgage-rate assumption, and other modeled assumptions.

Risk: Housing-market aggregates may be misleading when periods, property types, geographies, or sample sizes differ.

Mitigation: Compare matched periods and property types, preserve nulls and gaps, include activity counts and measurement windows, and avoid averaging medians across ZIP, city, or metro levels.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Redfin Data Center](https://www.redfin.com/news/data-center/)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/housing-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with comparison tables, optional time-series charts, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, measurement windows, units, missing-data notes, and API-derived housing-market statistics.]

## Skill Version(s):

1.0.9 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
