## Description:

health-check runs local project governance checks, reports P0/P1/P2 issues in plain language, and waits for user authorization before opening follow-up repair tasks through task-manager.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI project coordinators use this skill to inspect Vibe-governed projects for task status, contract, skill version, cross-module change, audit log, and TASKS formatting issues before deciding whether to open remediation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local shell checks that read project governance files, recent git history, and installed skill metadata under the user's home directory.

Mitigation: Review the shell script before installation and run it only from intended project roots.

Risk: The skill writes HEALTH_AUDIT.md and .health_state, and prior state can make later reports more severe.

Mitigation: Disclose this persistence to users and review the .workbuddy/memory state when investigating unexpected escalations.

Risk: Agent-level enforcement guidance can escalate or stop responses based on user choices.

Mitigation: Keep remediation decisions under human review and require explicit authorization before creating follow-up tasks or enabling any workflow-blocking behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/health-check)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text reports, Markdown audit entries, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append audit and state files under .workbuddy/memory when run.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter, skill.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
