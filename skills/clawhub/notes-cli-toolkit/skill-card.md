## Description:

An Obsidian notes automation skill that guides agents in using notesmd-cli for headless vault operations, frontmatter updates, daily note generation, and editor-based note workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and automation teams use this skill to have an agent plan or run notesmd-cli workflows for Obsidian vault maintenance, including bulk frontmatter edits, daily-note creation, archival, and CI-driven note updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk shell and write operations can change many Obsidian Markdown files in a vault.

Mitigation: Use a version-controlled or backed-up vault, run dry-runs first, and review affected files before applying bulk edits or moves.

Risk: The skill depends on executing notesmd-cli with access to local vault paths.

Mitigation: Install only when the notesmd-cli source is trusted and scope the agent's shell and write access to the intended vault.

Risk: Unclear scope and install safety can lead to use outside the intended notes automation workflow.

Mitigation: Limit use to Obsidian notes automation and avoid unrelated data-analysis tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/notes-cli-toolkit)
- [Declared homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations and file-change review guidance before bulk vault edits.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
