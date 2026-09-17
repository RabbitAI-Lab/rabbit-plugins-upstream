## Description:

Simple Analytics helps an agent use an OOMOL-connected account to inspect action schemas, list websites, retrieve stats, export datapoints, and send confirmed events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Simple Analytics through an OOMOL-connected account, including reading website analytics, exporting raw datapoints, and sending explicitly confirmed event or pageview data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute network-downloaded code during oo CLI setup.

Mitigation: Review the setup path before installing and prefer a verified, versioned, or signed oo CLI installation method.

Risk: Simple Analytics requests and responses route through OOMOL and may include sensitive exports, event payloads, or analytics data.

Mitigation: Confirm the data handling path is acceptable before using exports or sending analytics payloads.

Risk: The send_event action changes Simple Analytics state.

Mitigation: Confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [Simple Analytics homepage](https://simpleanalytics.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simple-analytics)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides live oo CLI schema inspection and connector execution; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
