## Description:

DNS Doctor helps agents scan, explain, and verify domain DNS and email-authentication issues through the DNS Doctor public API, returning deterministic findings and validated copy-paste DNS records instead of guessed fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and domain operators use this skill to diagnose email deliverability, DNS propagation, SPF, DMARC, DKIM, blacklist, MX, DNS health, and expiry issues, then present safe next steps and validated records for a human to publish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names and DNS troubleshooting inputs are sent to dnsdoctor.dev.

Mitigation: Install and use the skill only when that external API disclosure is acceptable for the domains being checked.

Risk: A DNSDOCTOR_API_TOKEN could expose account monitoring reads if pasted into chat or logs.

Mitigation: Keep the token in the execution environment and do not ask users to paste credentials into the conversation.

Risk: Publishing an incorrect DNS record can affect mail delivery or domain policy.

Mitigation: Review returned records before publishing them at the DNS host and have the domain owner apply changes.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor skill page](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API responses, findings, and copy-paste DNS records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns guidance for external DNS changes; the skill does not write DNS records itself.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
