## Description:

Diagnoses domain DNS and email-authentication issues, explains scan findings, and provides validated records for a human to publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Domain owners and administrators use this skill to investigate DNS and email-delivery issues, check propagation and look-alike domains, and review validated record suggestions before publishing changes themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names, DNS records, IPs, selectors, or pasted reports sent for analysis leave the user's environment; scan reports may be public.

Mitigation: Check with the user before sending sensitive data and do not scan domains they want kept private.

Risk: Monitoring reads use an account API token.

Mitigation: Supply DNSDOCTOR_API_TOKEN only through the user's environment; never ask for or disclose a pasted credential.

Risk: Calls beyond free limits may trigger x402 payments in a wallet-capable client.

Mitigation: Review payment behavior and costs before enabling a wallet-capable client.

Risk: Incorrectly published email-authentication records can disrupt legitimate mail.

Mitigation: Present validated records unchanged, explain blockers, and leave publication and approval to the domain owner.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor API schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor on ClawHub](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and DNS records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested records require human review and publication; the skill does not change DNS.]

## Skill Version(s):

1.10.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
