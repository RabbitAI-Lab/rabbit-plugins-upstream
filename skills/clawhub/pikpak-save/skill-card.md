## Description:

Guides users through manually saving authorized links to PikPak, checking a task by exact ID, and selectively restoring shared files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and assisting agents use this skill to submit an authorized magnet link, URL, or share link, track a specific task, and restore only approved shared files. It offers manual guidance and a local task-receipt checker, not a persistent batch job system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud tasks or downloads could use an account or link the user is not authorized to use.

Mitigation: Confirm account ownership and authorization for each link before taking action.

Risk: An ambiguous task result or broad share restoration could create duplicates or restore unapproved files.

Mitigation: Reconcile uncertain submissions manually and approve exact task, share, file, and destination IDs before continuing.

Risk: The optional referral code may benefit its sharer.

Mitigation: Disclose the referral and let the user decline it without affecting use of the skill.

## Reference(s):

- [PikPak Save on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-save)
- [Upstream design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions and local JSON task-status receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user approval for sensitive actions; does not provide persistent automation.]

## Skill Version(s):

1.0.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
