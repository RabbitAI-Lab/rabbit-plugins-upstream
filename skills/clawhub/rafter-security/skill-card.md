## Description:

Rafter Security helps agents and developers scan code and repositories for vulnerabilities, audit third-party skills and agent configurations, classify shell-command risk, and generate secure design questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to apply Rafter CLI checks for secrets, dependency and application scanning, command-risk validation, audit logs, and third-party skill reviews in AI-assisted development workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change agent behavior through integrations or hooks.

Mitigation: Install only after reviewing Rafter CLI trust, initialization flags, hook behavior, audit logging, output filtering, and disable controls.

Risk: Remote scans may send code or repository data to Rafter services when RAFTER_API_KEY is used.

Mitigation: Use offline rafter secrets for local-only secret scanning when remote analysis is not acceptable, and confirm data handling policies before running rafter run.

Risk: Command validation workflows may be confused with real command execution.

Mitigation: Confirm whether a command is only classified or actually executed before routing it through rafter agent exec or /rafter-bash.

## Reference(s):

- [Rafter homepage](https://rafter.so)
- [ClawHub skill page](https://clawhub.ai/rafter/skills/rafter-security)
- [ClawHub publisher profile](https://clawhub.ai/user/rafter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe CLI requirements such as the rafter binary and optional RAFTER_API_KEY; scan findings should be reviewed before acting.]

## Skill Version(s):

0.10.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
