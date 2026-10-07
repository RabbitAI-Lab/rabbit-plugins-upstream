## Description:

Organizes files in a local folder by extension, previewing proposed moves by default and moving files only when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text: All rights reserved

## Use Case:

People and agents organizing local folders can preview how files will be grouped by extension, then explicitly apply the proposed moves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying the plan moves local files and may disrupt existing folder organization.

Mitigation: Review the preview and back up important folders before using --apply.

Risk: The skill requests WebFetch permission although organizing local files does not require it.

Mitigation: Restrict WebFetch access or remove this permission when configuring the skill.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/dir-organizer)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Plain text or JSON file-move plan, with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview by default; --apply moves files after explicit confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
