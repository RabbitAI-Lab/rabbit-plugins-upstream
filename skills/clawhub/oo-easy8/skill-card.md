## Description:

Easy8 lets agents read, create, update, and delete Easy8 data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Easy8 projects and tasks through an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting Easy8 data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review or independently verify the oo CLI installer source before running curl-to-bash or PowerShell iex commands.

Risk: Write and destructive Easy8 actions can change or permanently delete project and task data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Easy8 homepage](https://www.easy8.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub Easy8 skill page](https://clawhub.ai/oomol/skills/oo-easy8)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON from the oo CLI when actions are executed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
