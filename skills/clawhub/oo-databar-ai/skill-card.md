## Description:

Databar.ai lets agents read, create, and update Databar.ai data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Databar.ai through an OOMOL-connected account, including reading account, table, row, enrichment, and task data. With user confirmation, it can also create tables, insert rows, and submit enrichment or waterfall tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review the setup path before installing and prefer official signed packages or separately downloaded, verified releases.

Risk: Write actions can create Databar.ai tables, insert rows, or submit enrichment and waterfall tasks.

Mitigation: Confirm the exact table, rows, action, and payload with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-databar-ai)
- [Databar.ai Homepage](https://databar.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
