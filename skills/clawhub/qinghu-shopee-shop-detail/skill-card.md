## Description:

Queries Shopee shop sales, revenue, product counts, and ratings for up to 10 shop IDs at a time through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and analysts use this skill to compare Shopee shops by sales, revenue, listing count, and ratings for a selected market and date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node may change the local environment beyond the data query.

Mitigation: Use a controlled environment with preinstalled, pinned tooling; review installation and upgrade steps before execution.

Risk: API access requires a token and paid calls consume Qinghu credits.

Mitigation: Review token setup, check the current credit estimate, and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-detail)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise shop comparison summary; table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 shop IDs per query; reports credit consumption for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
