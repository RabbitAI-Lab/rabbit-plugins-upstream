## Description:

DNS Doctor helps agents scan, explain, fix, and verify domain DNS health for email authentication, propagation, SPF supply-chain exposure, MX, blacklist, domain expiry, and TLS certificate checks through the DNS Doctor public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, operators, and support teams use this skill to diagnose email delivery and DNS health issues for domains, then present exact server-validated DNS records or verification guidance for a human domain owner to apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names, DNS records, IP addresses, or pasted DMARC data requested by the user are sent to dnsdoctor.dev.

Mitigation: Tell users what will be sent before checks involving sensitive domains or pasted data, and avoid scanning domains they want kept private.

Risk: Scan results are public report pages on dnsdoctor.dev.

Mitigation: Do not scan confidential or unreleased domains unless the user explicitly accepts that the report is public.

Risk: Optional API tokens and x402 payment are service features that can disclose account intent or spend funds.

Mitigation: Use tokens or x402-capable payment only when the user intentionally chooses those features, and never ask the user to paste credentials into chat.

Risk: Incorrectly rewriting DNS records can silently weaken email authentication or de-authorize legitimate senders.

Mitigation: Present service-returned DNS record strings exactly as returned, and leave publication of records to the human domain owner.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor ClawHub listing](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl command examples, diagnostic summaries, and exact DNS record strings when returned by the service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only diagnostics and human-applied DNS configuration guidance; it does not modify DNS or local files.]

## Skill Version(s):

1.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
