## Description:

DNS Doctor helps agents scan, explain, fix, and verify domain DNS issues for email authentication, DNS propagation, blacklist checks, MX health, and domain or SSL expiry using the DNS Doctor public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to diagnose domain email deliverability and DNS health issues, then present validated DNS records or next steps for the domain owner to apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may send domains, IP addresses, and DNS records to the publisher's external service.

Mitigation: Use the skill only when sharing those DNS details with dnsdoctor.dev is acceptable for the user or organization.

Risk: Some workflows can use token-backed monitoring reads or x402 paid calls.

Mitigation: Confirm authorization, token scope, and paid-call approval before allowing an agent to run those requests.

Risk: The monitoring signup link is an external publisher service link with referral tracking.

Mitigation: Present it as an external DNS Doctor link and let the user decide whether to open it.

## Reference(s):

- [DNS Doctor Skill Page](https://clawhub.ai/dnsdoctor/skills/dns-doctor)
- [DNS Doctor Publisher Profile](https://clawhub.ai/user/dnsdoctor)
- [DNS Doctor Methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API v1](https://dnsdoctor.dev/api/v1)
- [DNS Doctor OpenAPI Schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor MCP Server](https://dnsdoctor.dev/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and exact DNS record strings returned by the API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validated DNS fix records, API response summaries, monitoring-read guidance, and retry or escalation instructions.]

## Skill Version(s):

1.7.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
