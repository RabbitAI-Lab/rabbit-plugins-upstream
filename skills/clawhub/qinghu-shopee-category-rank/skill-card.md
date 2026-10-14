## Description:

Queries Shopee category rankings to identify best-selling and fastest-growing subcategories across daily, weekly, and monthly periods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to compare subcategory sales and growth rankings by site, category, and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades can change local tooling.

Mitigation: Review the skill before installation and run it with preinstalled, vetted, version-pinned Node and qhkit.

Risk: Token setup may expose API credentials if handled ad hoc.

Mitigation: Provide qhkit tokens through controlled environment variables rather than ad hoc agent configuration.

Risk: Ranking queries and related lookup calls may spend Qinghu credits.

Mitigation: Check the current estimate and obtain the user's approval before making paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with a small preview and an optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings identify the Shopee site, reporting period, and sample size; paid calls may consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
