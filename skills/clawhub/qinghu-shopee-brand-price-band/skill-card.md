## Description:

Queries Shopee brand price bands to summarize product and store counts, recent sales, and their shares by price range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to identify a brand's pricing distribution and compare product coverage and recent sales across price bands for a selected site and date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades can run unpinned npm software and change the local environment or persistent shell settings.

Mitigation: Review changes before execution; use a controlled environment with a trusted, pinned qhkit version and approve any installation or shell configuration changes explicitly.

Risk: Paid data queries can incur Qinghu credit charges, including when a service-side call fails.

Mitigation: Check estimated credits and obtain user approval before making paid calls; disclose actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-price-band)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summary with optional tabular data file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site, period, sample size, and credits charged when applicable.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
