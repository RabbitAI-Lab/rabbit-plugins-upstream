## Description:

Assesses Amazon market-entry viability for a named keyword or category using ZooData market, competitor, pricing, brand, trend, and review signals to produce a GO, CAUTION, or AVOID recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace analysts, and agent operators use this skill to evaluate whether a specific Amazon product niche or category is commercially attractive before market entry. It supports data-backed category research, competitor comparison, consumer pain-point analysis, and entry-strategy guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Amazon market research inputs, including keywords, category paths, ASINs, marketplace/date values, and review queries, to ZooData.

Mitigation: Use the skill only when those inputs are appropriate to share with ZooData, and avoid including unnecessary sensitive business context in prompts.

Risk: ZooData API calls consume account credits, and the full market-entry workflow can require many API calls.

Mitigation: Estimate credit usage before broad or ambiguous scans, confirm multi-call runs with the user, and use narrower granular commands when a credit cap applies.

Risk: The skill requires a ZooData API key and may read a local credential store if the environment variable is not set.

Mitigation: Prefer setting ZOODATA_API_KEY as an environment variable and avoid persistent credential storage unless local policy permits it.

Risk: Market-entry recommendations depend on sampled ZooData coverage and external API availability.

Mitigation: Review the confidence labels, data provenance, and API usage sections, and do not fabricate results when credentials, credits, or endpoint availability block evidence collection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-entry-analyzer)
- [Publisher Profile](https://clawhub.ai/user/apiclaw)
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData](https://zoodata.ai)
- [ZooData API Keys](https://zoodata.ai/en/api-keys)
- [ZooData API Field Reference](references/reference.md)
- [ZooData CLI Contract](references/cli-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown market-entry assessment with tables, confidence labels, API usage details, and optional shell commands for ZooData CLI execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. ZooData API calls consume account credits and send market research inputs such as keywords, category paths, ASINs, marketplace/date values, and review queries to ZooData.]

## Skill Version(s):

1.0.9 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
