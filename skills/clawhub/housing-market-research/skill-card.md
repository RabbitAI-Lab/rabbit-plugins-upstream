## Description:

Compare US housing markets through Crawlora's historical housing dataset and Redfin tools. Use for city, metro, county, or ZIP-code comparisons of prices, inventory, sales activity, time on market, and explicitly qualified affordability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to compare US city, metro, county, ZIP-code, or national housing-market trends across comparable periods. It supports market aggregate analysis, optional live Redfin context, and qualified affordability comparisons without treating aggregates as property valuations or personal financing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housing-market queries and the Crawlora API key are sent to Crawlora when live requests are run.

Mitigation: Keep the API key in the environment, review requests before execution, and avoid including unrelated sensitive data in query parameters or POST bodies.

Risk: Housing aggregates can be mistaken for individual property appreciation, precise neighborhood affordability, or personal mortgage qualification.

Mitigation: Label market aggregates clearly, preserve sample and activity counts, disclose affordability assumptions and income vintage, and keep custom financing scenarios separate from returned data.

Risk: Historical dataset rows and live Redfin context may represent different populations, dates, and units.

Mitigation: Keep historical aggregates and live listings or trends separate unless clearly labeled, and compare only matched periods and compatible geographies.

## Reference(s):

- [housing-market-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Redfin source and methodology](https://www.redfin.com/news/data-center/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with comparison tables, optional time-series charts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve measurement windows, units, sample or activity counts, source labels, collection time, assumptions, and missing-data notes.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
