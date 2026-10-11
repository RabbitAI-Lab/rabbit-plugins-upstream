## Description:

按类目查询 Shopee 店铺的日、周、月热销榜和飙升榜，并筛选店铺类型及本土或跨境店铺。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to compare top-selling and fast-rising shops by category, marketplace, and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade unpinned Node/npm tooling and change user-level environment settings.

Mitigation: Review installation steps before running them; preinstall a pinned, trusted qhkit version if preferred.

Risk: Ranking queries may consume Qinghu credits and send requested data scope to a paid service.

Mitigation: Check estimated credits and requested scope, then obtain approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranked-shop summaries; tabular files for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels results by marketplace, reporting period, and sample size.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
