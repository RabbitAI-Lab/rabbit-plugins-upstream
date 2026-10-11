## Description:

Makes WorkBuddy built-in skills visible in the installed-skill list and supports checking and restoring their copies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users and administrators can inspect missing built-in skills, make them visible through user-directory copies, compare copies with originals, and restore the prior state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sync makes persistent copies of built-in skills in the user skill directory.

Mitigation: Review list and status before syncing, and confirm the target directories.

Risk: Restore removes copied skills, while force options can overwrite or remove changed copies.

Mitigation: Run restore --dry-run, inspect the proposed removals, and confirm before proceeding; use --force only when needed.

Risk: Optional bundle commands modify WorkBuddy application files and may disrupt its interface.

Mitigation: Prefer copy-based sync; avoid bundle and bundle-restore unless you understand the impact and have a backup.

## Reference(s):

- [WorkBuddy Skill Visibility on ClawHub](https://clawhub.ai/wangjiaocheng/skills/workbuddy-skill-visibility)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Changes to copied skills take effect after a full WorkBuddy restart.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
