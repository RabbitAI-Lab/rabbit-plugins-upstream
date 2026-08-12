## Description:

DNS Doctor helps agents diagnose SPF, DMARC, DKIM, MX, DNS, blacklist, and domain or TLS expiry issues through the DNS Doctor public API, returning validated fix records instead of guessed DNS changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and domain owners use this skill to investigate email deliverability and domain-authentication failures, explain the findings, and provide exact DNS records or next steps for a human owner to apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain diagnostic data is sent to dnsdoctor.dev for scans and focused checks.

Mitigation: Use the skill only when the user is comfortable sending the domain diagnostic request to the disclosed external service.

Risk: API tokens for monitoring reads could be exposed if pasted into chat.

Mitigation: Do not ask users to paste credentials; have the account owner place any DNS Doctor token in the environment themselves.

Risk: Incorrect or premature DNS record publication can disrupt legitimate email delivery.

Mitigation: Keep DNS publication human-approved and present service-generated records exactly as returned.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor OpenAPI schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [ClawHub skill page](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, explanations, and exact DNS record strings when provided by the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API response excerpts; returned DNS record strings should be relayed verbatim.]

## Skill Version(s):

1.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
