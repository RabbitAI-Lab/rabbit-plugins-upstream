## Description:

SKILL1 helps agents organize local folders by type or date, batch rename files, clean empty directories and duplicates, and flatten nested directories with dry-run previews by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[q-ian-l](https://clawhub.ai/user/q-ian-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and other agent users can use this skill to tidy local working directories such as downloads, desktops, project folders, and photo folders after confirming the target path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Duplicate cleanup computes local file hashes, so files in the target directory are read locally even though nothing is uploaded.

Mitigation: Use the default preview mode first, target only the intended folder, and avoid sensitive directories unless local hashing is acceptable.

Risk: Commands run with --apply can move, rename, flatten, or delete files.

Mitigation: Review dry-run output before adding --apply and keep backups for important directories.

## Reference(s):

- [SKILL1 on ClawHub](https://clawhub.ai/q-ian-l/skills/skill1)
- [q-ian-l Publisher Profile](https://clawhub.ai/user/q-ian-l)
- [ClawHub](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and concise execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may propose preview commands first and use --apply only after explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
