## Description:

New Relic (newrelic.com). Use this skill for New Relic account operations, including reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other external users use this skill to operate a connected New Relic account through OOMOL, including querying observability data and managing dashboards, alerts, monitors, secure credentials, deployment markers, and snapshot URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a signed, package-manager-based, or otherwise independently verified installation path when available; only run remote installer scripts after verifying the source.

Risk: The skill can create, update, and delete New Relic resources through the connected account.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write or destructive action.

Risk: The activation wording is broader than necessary and could steer unrelated New Relic tasks through this connector.

Mitigation: Use the skill only for intended operations against the user's connected New Relic account.

## Reference(s):

- [New Relic homepage](https://newrelic.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-new-relic)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
