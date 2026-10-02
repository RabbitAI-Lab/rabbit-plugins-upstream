## Description:

Manage and maintain a shared Obsidian knowledge base by organizing files, performing task reviews, archiving, and ensuring up-to-date, linked knowledge content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diliumentu](https://clawhub.ai/user/diliumentu)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge workers and developers using an agent with an explicitly configured Obsidian vault use this skill to organize notes, record task retrospectives and skill-learning records, maintain links, and propose periodic cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad retention and cleanup behavior, including archiving and deletion in a knowledge-base folder.

Mitigation: Use it only with an explicitly configured knowledge-base folder, require approval before writes, moves, or deletions, and keep recoverable backups.

Risk: Private MEMORY.md storage can capture secrets or sensitive private data.

Mitigation: Avoid storing secrets or sensitive private data in MEMORY.md and review private notes before syncing, sharing, or exporting the vault.

Risk: The artifact contains trailing shell-like residue in SKILL.md.

Mitigation: Remove the trailing shell-like residue from SKILL.md before publication or installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/diliumentu/skills/knowledge-base-manager)
- [Publisher Profile](https://clawhub.ai/user/diliumentu)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Markdown guidance with Obsidian folder paths, maintenance rules, checklists, and note templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes recurring review cycles and templates for task retrospectives and skill-learning records.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
