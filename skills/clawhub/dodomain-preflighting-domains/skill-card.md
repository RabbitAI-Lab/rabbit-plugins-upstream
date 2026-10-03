## Description:

Checks a domain's DNS provider, registrable zone, connection options, and existing doDomain team connection before onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and customer-onboarding teams use this read-only preflight to explain DNS ownership and connection steps before starting a custom-domain connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking existing connections can reveal whether the doDomain team has a connection for a queried domain.

Mitigation: Use team-connection lookups only when that team-state check is appropriate, and share results only with the intended audience.

## Reference(s):

- [doDomain: Preflighting Domains on ClawHub](https://clawhub.ai/bsalaeddin/skills/dodomain-preflighting-domains)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only DNS and team-connection summary; reports detection uncertainty when applicable.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
