## Description:

Helps agents diagnose domain DNS and email authentication, explain findings, and present validated records for a human to publish and verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Domain owners, email administrators, and developers use this skill to investigate DNS and mail-delivery issues, review email authentication and look-alike domains, and verify human-applied DNS changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested domain scans go to DNS Doctor and scan reports may be public.

Mitigation: Check only domains the user is comfortable sharing with the service.

Risk: Credentials or DNS changes could be mishandled while following diagnostic guidance.

Mitigation: Do not ask the user to provide credentials to the agent; leave DNS publication to the human owner.

## Reference(s):

- [DNS Doctor on ClawHub](https://clawhub.ai/dnsdoctor/skills/dns-doctor)
- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown explanations with verbatim DNS records when the service provides them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and record suggestions are for human review and publication; the skill does not change DNS.]

## Skill Version(s):

1.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
