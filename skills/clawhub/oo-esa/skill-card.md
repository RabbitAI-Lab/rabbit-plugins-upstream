## Description:

esa (esa.io). Use this skill for ANY esa request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with esa teams through an OOMOL-connected account, including reading, searching, creating, updating, and deleting esa content through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can perform write and destructive esa actions, including deleting comments and rolling back post revisions.

Mitigation: Review exact payloads and target resources before approving write or destructive actions.

Risk: First-time setup may require installing the oo CLI before the skill can run.

Mitigation: Verify the oo CLI installer source before installation.

Risk: The skill operates on esa teams through an OOMOL-connected account.

Mitigation: Install only when the intended workflow permits agent access to the connected esa teams.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esa)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [esa homepage](https://esa.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; oo CLI command responses are JSON.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
