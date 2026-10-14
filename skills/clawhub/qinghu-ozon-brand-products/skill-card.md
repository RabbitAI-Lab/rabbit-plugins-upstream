## Description:

Queries Ozon brand products' sales over the last 28 days, with sorting by units sold, sales revenue, or price.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to find a brand's best-selling products and compare recent sales, revenue, and prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades of Node and qhkit can change the host environment.

Mitigation: Prefer a trusted, pre-provisioned, pinned qhkit installation; review and approve host setup before allowing changes.

Risk: Paid Qinghu queries consume credits, with charges that can increase with result volume.

Mitigation: Review the current estimate and expected query volume, obtain user approval before paid calls, and report actual credits spent.

Risk: The skill may use or store a Qinghu qhkit token.

Mitigation: Use a trusted account context and protect the token when configuring or using qhkit.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-brand-products)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise prose with key data previews and a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the Ozon reporting period, sample size, and credits spent on paid queries.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
