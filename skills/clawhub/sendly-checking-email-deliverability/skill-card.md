## Description:

Checks Sendly sending-domain health and delivery issues, then guides users through DNS setup, suppression review, and address validation with confirmation before changes or billed checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Sendly users and email administrators use this skill to diagnose delivery failures, check sending-domain authentication, review suppressions, and validate addresses before sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Sendly exposes domain status, bounce and suppression data, and email validation results to the agent.

Mitigation: Confirm that this access is acceptable before connecting Sendly.

Risk: Domain and suppression changes affect sending behavior; address validation and list cleaning are billed per address.

Mitigation: Confirm the exact domain or address before changes, and confirm the address count and cost exposure before validation or cleaning.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/sendly-checking-email-deliverability)

## Skill Output:

**Output Type(s):** [Text, Configuration guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports domain status and diagnosis, DNS records to publish, verification results, suppression counts, and validation results.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
