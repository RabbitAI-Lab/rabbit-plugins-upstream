## Description:

Helps agents plan and perform rule-based batch file renaming with prefixes, suffixes, numbering, find-and-replace, and extension filtering; changes require explicit confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can preview a plan for renaming files in a directory, then explicitly apply the changes after checking the proposed names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filename collisions or mistaken rules can cause unwanted renames.

Mitigation: Review the preview before using --apply, and back up important directories.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/batch-renamer)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Plain text or JSON rename preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview is the default; file names change only when --apply is used.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
