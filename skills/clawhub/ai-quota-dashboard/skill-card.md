## Description:

Provides a multi-provider AI quota dashboard and guidance for monitoring usage, balances, and reset times with developer API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to monitor AI provider credits, quotas, and reset times through a dashboard, and to configure secure collection and access to that telemetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored provider API credentials may be exposed through permissive file access or overly broad scopes.

Mitigation: Use read-only or limited-scope keys where possible and restrict the configuration file to its owner.

Risk: An internet-exposed dashboard may reveal private quota telemetry.

Mitigation: Keep access private or require authentication and HTTPS before exposing the dashboard to the internet.

Risk: Using browser session cookies for telemetry can expose account sessions.

Mitigation: Use official developer API keys or dedicated service tokens instead of browser session cookies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/synthet1x/skills/ai-quota-dashboard)
- [Provider telemetry integration guide](artifact/references/api-reverse-engineering.md)
- [Networking and deployment guide](artifact/references/networking-deployment.md)
- [Credential isolation and token management guide](artifact/references/security-cookie-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Code]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a dashboard template and a collector that writes JSON quota telemetry.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
