## Description:

OCR, tag, search, deduplicate, and organize screenshots. Makes screenshots searchable by content, detects and removes duplicates, groups by topic, and generates a searchable index. Use when a user has hundreds of unorganized screenshots and needs to find, clean, or categorize them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to scan large screenshot folders, identify duplicates, extract searchable OCR text, classify screenshots by content, and produce reports or organization plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR indexes can contain sensitive text from screenshots, including private messages, financial details, passwords, or personal identifiers.

Mitigation: Keep generated indexes local and private, avoid syncing them to shared cloud folders, and encrypt or delete indexes that contain sensitive content.

Risk: Duplicate detection and organization plans can recommend deleting or moving screenshots that still need human review.

Mitigation: Use report and dry-run modes first, review near-duplicate matches and target folders, and only run organization with execution enabled after confirming the plan.

## Reference(s):

- [Screenshot Organization Reference](references/classification_rules.md)
- [Source repository](https://github.com/voronindenis5/screenshot-organizer)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/screenshot-organizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, reports, JSON indexes, and organization plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local OCR text indexes, duplicate reports, searchable JSON data, and dry-run file organization plans.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
