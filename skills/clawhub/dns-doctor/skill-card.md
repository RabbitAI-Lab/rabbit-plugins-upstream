## Description:

Diagnoses domain DNS and email authentication, then presents validated fix records for a human to review and publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and domain administrators use this skill to diagnose DNS, mail delivery and authentication issues, check propagation, and review suggested records before publishing changes themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain scans are sent to DNS Doctor and may create public report pages.

Mitigation: Tell users before scanning and avoid domains they need to keep private.

Risk: An optional API token grants read-only access to account monitoring and email-test history.

Mitigation: Use a token only with the user's consent and send it only to the documented account endpoints.

Risk: Email tests retain verdicts and selected header facts; a redacted excerpt may be sent to an AI provider for optional hints.

Mitigation: Explain the disclosed retention and sharing before testing; avoid tests involving sensitive messages.

Risk: Incorrect or prematurely strengthened DNS records could disrupt legitimate mail.

Mitigation: Present validated records exactly as returned and require the domain owner's review and approval before publication.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API specification](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor ClawHub release](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and DNS records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested records are presented verbatim for human review; the skill does not change DNS records.]

## Skill Version(s):

1.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
