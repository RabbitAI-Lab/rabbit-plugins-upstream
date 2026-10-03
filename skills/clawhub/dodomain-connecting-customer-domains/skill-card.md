## Description:

Guides an agent through creating a doDomain connect session, sharing customer DNS records, and checking whether the domain is verified.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operators use this skill to onboard a customer's custom domain, provide the required DNS records, and check connection progress and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating a session for the wrong app, domain, or DNS records consumes monthly quota and opens a remote connection session.

Mitigation: Confirm the app, domain, and DNS records with the user before creating a session.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/dodomain-connecting-customer-domains)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a session token, DNS records to apply, and per-record verification status when available.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
