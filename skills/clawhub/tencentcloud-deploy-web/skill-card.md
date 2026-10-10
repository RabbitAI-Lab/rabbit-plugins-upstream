## Description:

Helps users deploy websites on Tencent Cloud and manage DNSPod records, SSL certificates, EdgeOne acceleration, and Lighthouse servers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use this skill to put websites online, configure domains and certificates, improve access from mainland China, and manage existing Tencent Cloud infrastructure. Purchases, identity verification, and regulatory filing remain with the user.

### Deployment Geography for Use:

Global; mainland China deployment and acceleration may require ICP filing.

## Known Risks and Mitigations:

Risk: Long-lived cloud credentials could expose DNS, CDN, and server resources if disclosed or misused.

Mitigation: Use a restricted Tencent Cloud subaccount for only intended resources; enter credentials through the local setup wizard or a platform secret store, never in chat; audit and revoke credentials when no longer needed.

Risk: Remote setup guidance allows cloud keys to be sent through chat when no secret store is available.

Mitigation: Do not use the chat fallback; provision a secure secret store or local setup before granting access.

Risk: Server command execution and persistent SSH keys can grant ongoing access to managed instances.

Mitigation: Review commands before execution and avoid adding persistent SSH keys unless continuing login access is deliberate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/claw-school/skills/tencentcloud-deploy-web)
- [Claw School homepage](https://claw-school.com)
- [Deployment routes](references/routes.md)
- [Human action cards](references/human-cards.md)
- [Source and verification notes](references/sources.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown with shell commands and user action cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report deployment status and provide website URLs; cloud operations require user-provided credentials.]

## Skill Version(s):

1.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
