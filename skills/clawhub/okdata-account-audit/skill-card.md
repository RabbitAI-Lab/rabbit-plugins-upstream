## Description:

Fetches one social media account's profile and latest page of posts, then presents the account figures alongside each post in a table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

People evaluating a social media account use the skill to compare profile totals with its latest posts across 11 supported platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account identifiers or profile links and API requests are sent to okdata, and calls may incur charges.

Mitigation: Use the service only for accounts the user asked about, state the maximum call cost before the first paid call, and keep the API key in environment or client configuration.

Risk: The security scan is incomplete because it could not resolve multiple local path-like references.

Mitigation: Review those references and the skill behavior before installation.

## Reference(s):

- [Account Audit skill documentation](https://okdata.online/skills/account-audit/?src=skill-okdata-account-audit)
- [账号体检诊断文档](https://okdata.online/zh/skills/account-audit/?src=skill-okdata-account-audit)
- [okdata agent connection guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table with account metrics and recent posts, followed by a brief assessment and source and cost details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One page of posts per account; unavailable metrics are left blank.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
