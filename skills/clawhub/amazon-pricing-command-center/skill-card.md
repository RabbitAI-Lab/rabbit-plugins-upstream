## Description:

Data-driven pricing strategy engine for Amazon sellers that analyzes ASINs with ZooData API data and returns RAISE, HOLD, or LOWER pricing guidance with profit simulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators, and supporting agents use this skill to evaluate ASIN pricing, competitor positioning, sales trends, and profit scenarios before making repricing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ASINs, category paths, keywords, marketplace/date values, and numeric filters to ZooData under the user's API key.

Mitigation: Install only when that data sharing is acceptable, and prefer the ZOODATA_API_KEY environment variable over a persistent shared config file.

Risk: API calls consume ZooData account credits, and batch or broad analyses can scale by ASIN count and category count.

Mitigation: Confirm expected credit cost before batch or broad analysis and stop when credential or credit errors are returned.

Risk: Pricing signals and recommended prices are decision support and may be misleading if treated as the sole basis for business action.

Mitigation: Use the report's confidence labels and validate pricing, FBA fees, demand, and competitive context with additional sources before acting.

## Reference(s):

- [Skill README](artifact/README.md)
- [ZooData CLI Contract](artifact/references/cli-contract.md)
- [ZooData API Field Reference](artifact/references/reference.md)
- [ZooData API Documentation](https://api.zoodata.ai/api-docs)
- [ZooData](https://zoodata.ai)
- [Metadata Homepage](https://github.com/SerendipityOneInc/ZooData-Skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with tables, command references, pricing signals, provenance, and API usage summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should match the user's language and label conclusions as data-backed, inferred, or directional.]

## Skill Version(s):

1.1.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
