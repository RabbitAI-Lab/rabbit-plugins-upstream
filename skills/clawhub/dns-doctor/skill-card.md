## Description:

DNS Doctor helps agents diagnose DNS and email-authentication issues for a domain through the DNS Doctor HTTPS API and return validated findings and fix records without guessing DNS records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and domain owners use this skill to investigate email delivery, SPF, DMARC, DKIM, DNS propagation, blacklist, MX, DNS health, and domain or SSL expiry issues. It guides the agent to run DNS Doctor reads, explain findings, present validated records verbatim, and verify human-applied DNS changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names, IP addresses, DNS records, and related diagnostic context submitted for checks are sent to dnsdoctor.dev.

Mitigation: Use the skill only when that external diagnostic disclosure is acceptable, and submit only the domains and records needed for the user's task.

Risk: Monitoring reads can expose account-specific monitoring data for verified domains when a DNS Doctor token is available.

Mitigation: Do not ask users to paste credentials in chat; require the account owner to place the token in the environment and use it only for the documented read-only endpoints.

Risk: Incorrectly edited DNS records can weaken email authentication or de-authorize legitimate senders.

Mitigation: Present server-returned fix records exactly as given, do not invent SPF or DKIM records, and leave DNS publication to the human owner.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor MCP server](https://dnsdoctor.dev/mcp)
- [ClawHub skill listing](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, DNS record strings, and plain-language findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned DNS records must be presented exactly as supplied by DNS Doctor; monitoring reads require a user-provided environment token and remain read-only.]

## Skill Version(s):

1.7.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
