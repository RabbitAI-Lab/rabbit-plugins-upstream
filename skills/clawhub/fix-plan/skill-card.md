## Description:

Manages the structure, prioritization, updates, and synchronization of local fix-plan and checklist files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project teams use this skill to maintain planning checklists, triage blocked work, and reconcile task status with linked issues and pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private local agent data and hook or profile configuration beyond checklist files.

Mitigation: Review hook resources and workspace profiles before use; avoid enabling it where local agent data must remain untouched.

Risk: Optional tracker integrations can modify external issues or comments and local planning state.

Mitigation: Enable integrations only in intended workspaces, review proposed changes, and use dry-run modes where available.

## Reference(s):

- [fix-plan release on ClawHub](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Checklist format guide](format.md)
- [Issue and pull request sync guide](sync.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown checklist updates and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update local planning files and synchronize linked tracker status.]

## Skill Version(s):

0.17.1 (source: ClawHub release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
