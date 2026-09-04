## Description:

DNS Doctor helps agents scan, explain, and verify domain DNS and email-authentication issues through DNS Doctor APIs, returning server-generated fix records for supported findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and email operations teams use this skill to diagnose DNS and email authentication problems, review server-provided findings, and give domain owners exact records or next steps to apply at their DNS host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names and DNS diagnostic queries are sent to dnsdoctor.dev.

Mitigation: Use the skill only for domains the requester is authorized to inspect and disclose that diagnostics are performed by the DNS Doctor service.

Risk: Optional token-based monitoring can expose a verified account's DNS alert and readiness data to the agent environment.

Mitigation: Do not paste credentials into chat; use an environment variable only when monitoring reads are needed and keep token handling under the account owner's control.

Risk: Incorrect DNS changes can disrupt email authentication or delivery.

Mitigation: Keep final DNS changes under the domain owner's approval, present server-returned records exactly as given, and verify published changes after the owner applies them.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor OpenAPI schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor MCP endpoint](https://dnsdoctor.dev/mcp)
- [DNS Doctor on ClawHub](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and DNS record strings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns DNS diagnostics and server-generated DNS records when supported; it does not directly modify DNS.]

## Skill Version(s):

1.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
