## Description:

Checks specific product, listing, and job URLs for current availability and supports one-time page conditions, 30-day change watchers, and submission or order confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moyecj-snap](https://clawhub.ai/user/moyecj-snap)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can check whether a specific listing, product, or job posting remains available before recommending, buying, or applying. They can also check page conditions, watch for changes, and confirm submissions or orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote CLI commands are suggested for wallet operations and paid checks.

Mitigation: Review the CLI before installing and use a pinned, reviewed agentcash version rather than @latest.

Risk: Checking private or tokenized URLs could disclose sensitive information to the service.

Mitigation: Use only specific URLs you intend to check and avoid private order or tokenized URLs unless necessary.

Risk: Watchers use webhook secrets and owner tokens that grant access to notifications or history.

Mitigation: Protect webhook secrets and owner tokens, and use a public HTTPS callback only when needed.

## Reference(s):

- [Livecheck on ClawHub](https://clawhub.ai/moyecj-snap/skills/livecheck)
- [Getting Started](rules/getting-started.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability is reported as live, closed, or unknown with supporting signals; watchers can send signed webhooks.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
