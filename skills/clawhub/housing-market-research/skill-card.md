## Description:

Compare US housing markets through Crawlora's historical housing dataset and Redfin tools. Use for city, metro, county, or ZIP-code comparisons of prices, inventory, sales activity, time on market, and explicitly qualified affordability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to compare US housing markets across city, metro, county, ZIP-code, or national geographies using Crawlora housing-market endpoints and optional Redfin context. It supports comparison tables, time-series charts, and qualified affordability analysis while keeping market aggregates separate from individual valuations or financing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an overridden destination if CRAWLORA_API_BASE is changed.

Mitigation: Use the default Crawlora API base or only set CRAWLORA_API_BASE to an endpoint you control and trust; prefer a limited or disposable API key when available.

Risk: The bundled script is broader than the stated housing-market purpose and can be run with arbitrary supported Crawlora paths.

Mitigation: Run the helper only with trusted arguments and review calls before using a real Crawlora key.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Redfin source and methodology](https://www.redfin.com/news/data-center/)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/housing-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with comparison tables, optional time-series chart guidance, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, collection time, measurement windows, units, sample/activity counts, and missing-data notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
