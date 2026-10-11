## Description:

Looks up a single Amazon ASIN's product details, including category, sales rank, price, reviews, sellers, variants, and listing indicators through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product researchers use this skill to retrieve details for one ASIN in a specified marketplace and review the listing's pricing, ranking, reviews, sellers, and variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt persistent Node or CLI installation and changes to the local environment.

Mitigation: Review the qhkit package and install it yourself in an isolated environment before running the skill.

Risk: Using the external API requires a token and may incur charges.

Mitigation: Use an ephemeral token variable rather than persistent configuration; check estimated credits and approve paid calls before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-asin-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with product data and optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the marketplace and credits charged; larger responses may be delivered as files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
