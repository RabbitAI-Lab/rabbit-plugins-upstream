## Description:

Helps users deploy websites on Tencent Cloud and manage DNS, certificates, CDN, and Lighthouse servers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

People without cloud-operations experience use this skill with an agent to publish websites, configure domains and HTTPS, and troubleshoot access through Tencent Cloud. The user handles purchases, identity verification, and required filings.

### Deployment Geography for Use:

Global; mainland China hosting and CDN may require ICP filing.

## Known Risks and Mitigations:

Risk: Long-lived cloud credentials could enable unauthorized changes to DNS, CDN, or server settings.

Mitigation: Use a scoped sub-account and local setup or platform secret storage; review audit logs and rotate credentials when access is no longer needed.

Risk: Server command execution can run arbitrary commands as root.

Mitigation: Limit the agent's access to intended resources and review server commands before execution.

## Reference(s):

- [Publisher homepage](https://claw-school.com)
- [Deployment routes](references/routes.md)
- [User action cards](references/human-cards.md)
- [Sources and verification notes](references/sources.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and user action cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment URLs and verification results.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
