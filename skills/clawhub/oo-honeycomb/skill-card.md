## Description:

Honeycomb (honeycomb.io) helps agents read, create, and update Honeycomb data through the OOMOL-connected Honeycomb connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to inspect Honeycomb account metadata, datasets, boards, and markers, and to create Honeycomb markers through the OOMOL-connected Honeycomb connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Honeycomb requests and responses are routed through OOMOL's connector, and OOMOL-held server-side credentials can exercise the connected Honeycomb permissions.

Mitigation: Install only if that routing and credential model is acceptable, and prefer narrowly scoped Honeycomb credentials.

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installer manually or use a verified package source before running installer commands.

Risk: The create_marker action changes Honeycomb state.

Mitigation: Confirm the exact marker payload and expected effect with the user before running write actions.

## Reference(s):

- [Honeycomb homepage](https://www.honeycomb.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-honeycomb)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
