## Description:

Screenshot Organizer helps agents OCR, tag, search, deduplicate, and organize large screenshot collections into searchable indexes and content-based folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and knowledge workers use this skill to triage large local screenshot folders, find screenshots by OCR text, identify duplicates, and plan folder organization before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR indexes can store sensitive screenshot text, including private messages, financial details, account information, and other personal data, in plaintext JSON.

Mitigation: Run the skill only on screenshot folders the user has approved, keep generated indexes in a private local folder, avoid syncing them to shared cloud storage, and delete indexes when they are no longer needed.

Risk: Execute mode can move screenshot files and filename collisions may overwrite files in organized folders.

Mitigation: Run report and dry-run workflows first, review the proposed organization plan, and make a backup before using execute mode on irreplaceable screenshot collections.

## Reference(s):

- [Screenshot Organizer ClawHub Skill](https://clawhub.ai/voronindenis5/skills/screenshot-organizer)
- [Source repository](https://github.com/voronindenis5/screenshot-organizer)
- [Screenshot Organization Reference](references/classification_rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell command examples; command outputs include human-readable reports and local JSON indexes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce deduplication reports, deletion plans, OCR extraction indexes, entity summaries, proposed folder structures, and moved screenshot files when execute mode is used.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
