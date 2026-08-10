## Description:

Comprehensive listing health check and optimization engine for Amazon sellers that scores listings across eight dimensions, benchmarks against category leaders, identifies keyword gaps, and generates data-backed improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, agencies, and marketplace operators use this skill to audit single or bulk Amazon listings, compare them with category leaders, and prioritize listing improvements using ZooData API evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASINs, keywords, category paths, marketplace and date values, and numeric filters are sent to ZooData for audits.

Mitigation: Install and use the skill only when those listing and market inputs are appropriate to share with ZooData.

Risk: Audit workflows consume ZooData account credits, especially multi-call listing scans.

Mitigation: Review estimated credit cost before broad or ambiguous scans and prefer narrower commands when operating under a credit cap.

Risk: A ZooData API key may be read from local configuration on machines that are shared with others.

Mitigation: Prefer setting ZOODATA_API_KEY in the environment and avoid storing shared credentials in ~/.zoodata/config.json on shared machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-listing-audit-pro)
- [ZooData-Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API documentation](https://api.zoodata.ai/api-docs)
- [ZooData API key setup](https://zoodata.ai/en/api-keys)
- [Listing Audit Pro API Field Reference](references/reference.md)
- [ZooData CLI Contract](references/cli-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown listing audit report with scorecards, comparison tables, suggested rewrites, data provenance, and API usage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Matches the user's language and labels conclusions as data-backed, inferred, or directional.]

## Skill Version(s):

1.0.8 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
