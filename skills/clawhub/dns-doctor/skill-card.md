## Description:

DNS Doctor diagnoses domain DNS and email authentication, explains findings, and provides validated DNS records for a person to review and publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and domain operators use the skill to diagnose DNS health and email authentication, investigate propagation and related domain signals, and review validated configuration fixes. It leaves publishing DNS changes to the human operator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan reports are public, and excerpts from a test email may be shared with an AI provider.

Mitigation: Avoid domains that must remain private and use a non-sensitive test email.

Risk: Publishing a DNS recommendation can affect domain services, and paid calls may incur charges.

Mitigation: Review proposed records before publishing and authorize paid calls deliberately; enable account access only when needed.

## Reference(s):

- [DNS Doctor Methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor](https://dnsdoctor.dev)
- [ClawHub Skill Release](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [DNS diagnostic summaries with copyable DNS records and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed DNS changes are presented for human review and publication.]

## Skill Version(s):

1.14.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
