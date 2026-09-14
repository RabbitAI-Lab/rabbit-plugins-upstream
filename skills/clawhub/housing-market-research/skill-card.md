## Description:

Compare US housing markets through Crawlora's historical housing dataset and Redfin tools. Use for city, metro, county, or ZIP-code comparisons of prices, inventory, sales activity, time on market, and explicitly qualified affordability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare U.S. housing markets across cities, metros, counties, or ZIP codes using Crawlora's historical dataset and optional Redfin context. It supports comparison tables, chart-ready time series, and qualified affordability discussion while separating market aggregates from personal valuation or financing advice.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Housing-market queries, optional locations, and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the API key in the environment, review requests before running the helper, and use the skill only when sending those queries to Crawlora is acceptable.

Risk: Affordability outputs may be mistaken for personal mortgage qualification or budget advice.

Mitigation: Present affordability as a modeled market comparison and disclose the stated assumptions, including income vintage, mortgage rate, down payment, tax and insurance estimate, and payment-to-income ratio.

Risk: Live Redfin context and historical market aggregates can have different populations, dates, and units.

Mitigation: Label each source separately, preserve measurement windows and units, and avoid blending live listings with historical aggregates into a single unlabeled statistic.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Redfin Data Center](https://www.redfin.com/news/data-center/)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/housing-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, optional chart-ready series, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include region, property type, measurement window, units, source, collection time, and missing-data notes when relevant.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
