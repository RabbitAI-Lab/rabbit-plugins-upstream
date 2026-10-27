## Description:

Routes TODO checklists to session tasks, project files, or shared issues and guides task reporting and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to keep session tasks, project checklists, and shared issues in the appropriate place while reporting progress consistently.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating shared issues can publish task details to an external tracker.

Mitigation: Require explicit user confirmation before creating Plane or GitHub issues and review the content to be shared.

Risk: Deleting or pruning tasks can remove persistent task history.

Mitigation: Confirm the target session and obtain explicit approval before deleting prior-session tasks or running prune or purge; preview prune results first.

Risk: An explicit task directory can redirect changes outside normal task storage.

Mitigation: Verify the target path and require explicit confirmation before using --dir outside the normal task directories.

## Reference(s):

- [TodoWrite on ClawHub](https://clawhub.ai/drumrobot/skills/todowrite)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON task records]

**Output Format:** [Markdown instructions and reports, with optional local JSON task ledgers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tasks may be routed to session ledgers, project checklists, or shared issue trackers.]

## Skill Version(s):

0.11.0 (source: ClawHub release and CHANGELOG; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
