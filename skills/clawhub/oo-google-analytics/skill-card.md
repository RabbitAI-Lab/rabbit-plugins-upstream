## Description:

Operates Google Analytics through an OOMOL-connected account for reading reports, discovering property metadata, and updating supported property configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to query Google Analytics accounts and GA4 properties, run standard, realtime, pivot, and batch reports, and manage supported custom dimensions, metrics, retention, and property settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Analytics requests and results are routed through OOMOL as a third-party connector.

Mitigation: Install only when that data routing is acceptable, grant only the scopes needed, and avoid sending unnecessary sensitive analytics data.

Risk: The setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer official, pinned, verifiable installation instructions and independently verify installer source and integrity before execution.

Risk: Supported write actions can create, archive, or update Google Analytics configuration.

Mitigation: Review the live action schema, exact payload, target property, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-analytics)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Analytics](https://analytics.google.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
