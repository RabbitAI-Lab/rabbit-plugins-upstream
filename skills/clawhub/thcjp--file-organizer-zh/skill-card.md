## Description:

文件 is a Chinese-language file organizer skill that helps agents classify files by type, identify duplicate files, and return processing status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to organize folders, classify files by type, and clean duplicate files through a Chinese-language agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read/write file authority and potential command or API authority.

Mitigation: Use it first on a small test folder, keep backups, restrict work to selected non-sensitive directories, and avoid sharing API keys unless data handling is understood.

Risk: File classification or duplicate cleanup can move, alter, or remove unintended files if the instruction or target path is too broad.

Mitigation: Review proposed operations and results before bulk execution, and prefer dry runs or restorable backups for important folders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-organizer-zh)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON status examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe file operations, execution status, errors, and follow-up checks.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
