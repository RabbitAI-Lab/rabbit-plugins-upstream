## Description:

Finds and replaces literal or regex text across files, previewing matches by default and backing up files before applied changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (ClawHub metadata); MIT (bundled Python code only); documentation and theoretical text: All rights reserved

## Use Case:

Developers and other agents use this skill to preview and perform bulk text replacements across files, including literal and regular-expression matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying a broad file glob can change many matched files.

Mitigation: Preview matches first, review broad globs, and keep backups of important data before using --apply.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/text-replace)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Plain-text or JSON match summary; edited text files only when --apply is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to preview mode; creates .bak backups before edits.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
