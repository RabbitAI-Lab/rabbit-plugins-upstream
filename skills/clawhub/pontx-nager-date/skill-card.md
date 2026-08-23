## Description:

Use for Nager.Date Community API v4 public-holiday integration, country or holiday lookups, commercial-use eligibility checks, and direct read-only SDK or CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Nager.Date Community API v4 holiday and country lookups through Pontx discovery, SDK, and CLI workflows. It helps teams keep reads narrow, reproducible, and aligned with provider use eligibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commercial or user-facing use may violate provider terms if sponsorship or entitlement is not confirmed.

Mitigation: Confirm active Nager.Date sponsorship or provider entitlement before production reads, redistribution, or paid-product integration.

Risk: Holiday data, country codes, subdivision codes, or timezone assumptions may be applied too broadly or incorrectly.

Mitigation: Resolve current endpoint constraints, preview narrow read requests, and surface upstream availability separately from application date logic.

Risk: Bulk collection, unbounded retries, or inappropriate caching could exceed the intended narrow read-only workflow.

Mitigation: Keep calls scoped to caller needs and cache only when provider terms and application policy permit.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API integration guidance; no credentials or mutation endpoints are described.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
