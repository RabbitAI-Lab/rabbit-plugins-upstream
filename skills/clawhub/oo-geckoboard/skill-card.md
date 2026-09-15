## Description:

Use this skill for Geckoboard requests, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Geckoboard datasets through an OOMOL-connected account, including appending, replacing, creating, and deleting dataset data after checking live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a downloaded oo CLI installer directly in the shell.

Mitigation: Use a verified, pinned, or inspectable installation method for the oo CLI before trusting the skill.

Risk: The skill can write, replace, or delete Geckoboard dataset data.

Mitigation: Inspect the live action schema and confirm the exact dataset, payload, and expected effect with the user before approving write or destructive actions.

## Reference(s):

- [Geckoboard homepage](https://www.geckoboard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-geckoboard)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
