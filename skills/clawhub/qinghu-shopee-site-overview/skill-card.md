## Description:

Helps agents retrieve and summarize Shopee site-level sales, revenue, active listing counts, and average order value using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers and analysts use this skill to compare Shopee site-level market activity and summarize sales, revenue, active listings, and average order value over a requested period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating Node and qhkit can change the host environment, particularly when versions are not pinned.

Mitigation: Prefer a preinstalled, pinned, platform-managed qhkit; require explicit approval before npm, npx, PATH, or shell-profile changes.

Risk: Configuring a Qinghu API token and making paid calls can expose credentials or consume credits.

Mitigation: Require explicit approval before token configuration, review estimated credit costs, and obtain consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-site-overview)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written analysis with optional tabular file export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identify the site and date range; report credit usage for paid calls and use full results rather than previews for large datasets.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
