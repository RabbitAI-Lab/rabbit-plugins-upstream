## Description:

Wrike helps agents read, create, and update Wrike tasks, folders, projects, and contacts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Wrike through an agent, including task search and retrieval, folder and project workflows, contact listing, and confirmed creation of tasks or folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can ask the user to execute remote installer scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a pinned, verifiable oo CLI release or official package manager installation.

Risk: Write actions can create or change Wrike tasks and folders.

Mitigation: Confirm the exact JSON payload and expected effect with the user before running any write-tagged action.

## Reference(s):

- [Wrike homepage](https://www.wrike.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Wrike skill page](https://clawhub.ai/oomol/skills/oo-wrike)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect live connector schemas before execution and requires user confirmation before write actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
