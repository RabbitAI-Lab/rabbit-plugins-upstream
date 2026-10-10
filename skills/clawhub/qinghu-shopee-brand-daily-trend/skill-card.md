## Description:

Queries daily Shopee brand trends by brand and site, including product count, sales volume, revenue, and shop count for up to 720 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to review daily brand sales and assortment trends across supported Shopee sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install or upgrade Node and qhkit and configure an API token without clear prior approval.

Mitigation: Require confirmation before local environment changes; preferably install a reviewed, pinned qhkit version yourself and configure the token securely.

Risk: Brand-trend queries can incur Qinghu credit charges.

Mitigation: Describe expected charges and obtain user approval before paid calls; report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-daily-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Text, Files]

**Output Format:** [Concise prose with trend figures and optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site and date range; paid calls report Qinghu credits consumed.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
