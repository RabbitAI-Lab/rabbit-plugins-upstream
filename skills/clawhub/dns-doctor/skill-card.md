## Description:

Helps agents diagnose DNS and email authentication issues, explain validated findings, and present DNS records for a person to publish and verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Domain owners, mail administrators, and developers use this skill to investigate delivery and DNS health, review suggested records, and confirm changes after publishing them themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domains and DNS records submitted for checks leave the user's environment, and scan results are public.

Mitigation: Confirm the user is comfortable sharing the domain and avoid scanning domains that must remain private.

Risk: Account-specific monitoring reads use an optional API token.

Mitigation: Only use a token the user has set in DNSDOCTOR_API_TOKEN; do not request or disclose credentials.

Risk: Calls beyond the free limit may prompt for x402 payment.

Mitigation: Review any payment prompt with the user before authorizing a paid call.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor ClawHub release](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with diagnostic findings and verbatim DNS record suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DNS changes require human publication; scans may produce public report pages.]

## Skill Version(s):

1.10.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
