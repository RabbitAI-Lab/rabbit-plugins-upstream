## Description:

Baremetrics (baremetrics.com). Use this skill for ANY Baremetrics request: reading, creating, and updating data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage Baremetrics sources, customers, plans, subscriptions, and charges through an OOMOL-connected account. It supports schema-first command execution and requires confirmation before write or cancellation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running remote installer scripts without reviewing the downloaded file.

Mitigation: Use an official installer path that allows review and verification before execution.

Risk: Write and cancellation actions can change Baremetrics customer, plan, subscription, or cancellation state.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write or cancellation command.

## Reference(s):

- [Baremetrics homepage](https://baremetrics.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return JSON responses with data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
