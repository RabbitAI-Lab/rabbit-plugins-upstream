## Description:

Use this Nozbe (nozbe.com) skill for reading, creating, updating, and deleting Nozbe data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Nozbe teams, projects, tasks, and comments through an OOMOL-connected account. It supports reading Nozbe data and, with user confirmation, creating, updating, or deleting supported resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute arbitrary code if the installer source is not trusted.

Mitigation: Review and verify the OOMOL installer through a safer, versioned, or signed installation method before running the documented install commands.

Risk: Write and destructive Nozbe actions can change or remove projects, tasks, and comments.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Nozbe Skill](https://clawhub.ai/oomol/skills/oo-nozbe-teams)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Nozbe Homepage](https://nozbe.com)
- [Nozbe Connector Icon](https://static.oomol.com/logo/third-party/nozbe_teams.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; command responses may include JSON data and an execution ID.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
