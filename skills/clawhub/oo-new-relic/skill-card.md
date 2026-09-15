## Description:

New Relic (newrelic.com). Use this skill for New Relic requests that read, create, update, or delete data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and site reliability teams use this skill to operate New Relic from an agent session, including querying observability data and managing dashboards, alerts, monitors, deployments, and secure credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote oo CLI installer commands that could install unverified code if run automatically.

Mitigation: Install oo only through a trusted, verified method and do not allow an agent to run installer commands automatically.

Risk: The skill can create, update, or delete New Relic resources.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-new-relic)
- [New Relic](https://newrelic.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include live schema inspection commands, New Relic action payload guidance, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
