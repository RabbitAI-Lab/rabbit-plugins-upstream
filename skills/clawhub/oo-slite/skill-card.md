## Description:

Slite integration for reading, creating, updating, and deleting Slite data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Slite through an OOMOL-connected account, including reading, searching, creating, updating, and deleting Slite notes and groups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users or agents to execute remote installer scripts with shell execution.

Mitigation: Review the installer source before use and prefer a pinned, signed, or otherwise independently trusted installation method where available.

Risk: The skill can create, update, and delete Slite content.

Mitigation: Confirm exact payloads and target records with the user before write or destructive actions.

## Reference(s):

- [ClawHub Slite Skill](https://clawhub.ai/oomol/skills/oo-slite)
- [Slite Homepage](https://slite.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Slite connector JSON responses for executed actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
