## Description:

查询 Shopee 各站点和类目的品牌热销榜与飙升榜，支持日榜、周榜和月榜。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to compare top-selling or fast-growing brands by site, category and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit or Node.js changes the host environment and depends on external packages.

Mitigation: Review the package and installation steps before execution; prefer a sandbox and explicitly approve host-level installs.

Risk: Configuring the Qinghu API token may leave credentials in persistent host configuration.

Mitigation: Use a managed secret store or environment variable where possible; avoid saving tokens to persistent configuration.

Risk: Brand-ranking queries may consume paid Qinghu credits.

Mitigation: Estimate charges and obtain explicit approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise brand-ranking analysis with key figures and optional table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes site and reporting period; paid calls report Qinghu credit usage.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
