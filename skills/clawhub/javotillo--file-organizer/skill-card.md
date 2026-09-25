## Description:

Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javotillo](https://clawhub.ai/user/javotillo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze messy local folders, detect duplicates, propose safer file structures, and execute approved cleanup or organization plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect broad local folder contents while analyzing files for organization.

Mitigation: Start with a specific non-sensitive directory, exclude system and sensitive folders, and review the analysis before allowing file operations.

Risk: Move, rename, or delete recommendations could affect important files if approved without review.

Mitigation: Review proposed moves and deletions carefully, keep backups for important files, and require confirmation before destructive changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/javotillo/skills/file-organizer)
- [ClawHub publisher profile](https://clawhub.ai/user/javotillo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command examples and proposed file-operation plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include summaries of inspected folders, duplicate candidates, proposed moves, deletion recommendations, and maintenance tips.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
