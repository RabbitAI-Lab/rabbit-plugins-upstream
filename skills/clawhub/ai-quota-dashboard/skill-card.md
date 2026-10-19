## Description:

Guides setup of a multi-provider AI quota dashboard with credential handling, usage monitoring, and deployment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure a dashboard for monitoring AI provider credits, quotas, and reset times across accounts and self-hosted services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored provider API keys or refresh tokens could be exposed through an improperly protected configuration file.

Mitigation: Use dedicated read-only credentials where possible, avoid browser cookies, and keep the configuration directory and files owner-only.

Risk: A publicly reachable dashboard could disclose private quota and account telemetry.

Mitigation: Keep access on a restricted local network or VPN; require authentication and HTTPS for public access.

## Reference(s):

- [AI Quota Dashboard release](https://clawhub.ai/synthet1x/skills/ai-quota-dashboard)
- [Credential isolation and token management](references/security-cookie-guide.md)
- [Provider telemetry integration](references/api-reverse-engineering.md)
- [Networking and deployment](references/networking-deployment.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command, configuration, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dashboard coverage depends on configured providers and available quota endpoints.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
