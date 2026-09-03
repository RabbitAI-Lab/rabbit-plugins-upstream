## Description:

OCR, tag, search, deduplicate, and organize screenshots. Makes screenshots searchable by content, detects and removes duplicates, groups by topic, and generates a searchable index. Use when a user has hundreds of unorganized screenshots and needs to find, clean, or categorize them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and knowledge workers use this skill to scan screenshot folders, identify duplicates, extract searchable OCR text, classify screenshots by content, and plan folder organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screenshots can contain private messages, financial information, credentials, or other sensitive details that may be captured in a generated text index.

Mitigation: Run report or dry-run modes first, review the target folder before processing, and keep generated JSON indexes private and out of cloud sync.

Risk: Deduplication and organization workflows can propose deletions or move files, and near-duplicates may not be safely interchangeable.

Mitigation: Review the move or deletion plan, make a backup, and use --execute only after confirming the proposed actions.

## Reference(s):

- [Screenshot Organization Reference](references/classification_rules.md)
- [Server-resolved source repository](https://github.com/voronindenis5/screenshot-organizer)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/screenshot-organizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python shell commands, text reports, and JSON index or scan outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local JSON indexes and dry-run plans; file moves require explicit execution.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
