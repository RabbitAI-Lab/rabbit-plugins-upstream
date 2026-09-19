## Description:

DNS Doctor helps agents diagnose domain DNS and email authentication issues, verify propagation, and present validated fix records for a human to publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to troubleshoot email deliverability and DNS health, audit SPF, DKIM, DMARC, MX, blacklist, registration, and TLS findings, and guide domain owners through verified DNS fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names and DNS records requested by the user are sent to dnsdoctor.dev, and scan results are public report pages.

Mitigation: Use the skill only for domains the user is comfortable making public, and avoid scanning domains that must remain private.

Risk: The optional DNSDOCTOR_API_TOKEN may grant access to account monitoring reads.

Mitigation: Use the token only from the environment and do not ask users to paste credentials into the conversation.

Risk: After free limits, x402-capable clients may encounter disclosed per-call payments.

Mitigation: Treat payment-required responses as a prompt to slow down, use a token, or proceed only when the client is intentionally configured for x402 payment.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [ClawHub skill page](https://clawhub.ai/dnsdoctor/skills/dns-doctor)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor MCP server](https://dnsdoctor.dev/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, diagnostic summaries, and DNS record strings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns read-only diagnostic guidance and validated records for human publication; requires curl and outbound HTTPS to dnsdoctor.dev.]

## Skill Version(s):

1.9.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
