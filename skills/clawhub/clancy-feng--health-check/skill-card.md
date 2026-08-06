## Description:

Vibe Health Check runs local project governance health checks, reports P0/P1/P2 findings in user-facing language, and waits for authorization before any repair task is created.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this skill to scan an AI project for governance issues such as task status consistency, contract completeness, skill version drift, cross-module changes, oversized audit logs, and TASKS formatting. It produces a diagnostic report and guides the user toward authorized follow-up work instead of changing project files directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health-check runs create local audit and state files under .workbuddy/memory.

Mitigation: Use clear invocation wording, review HEALTH_AUDIT.md periodically, and avoid installing this skill when a strictly read-only diagnostic workflow is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/health-check)
- [Publisher profile](https://clawhub.ai/user/clancy-feng)
- [Skill README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain-text diagnostic report with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append local audit and state records under .workbuddy/memory during health-check runs.]

## Skill Version(s):

1.0.0 (source: release evidence, skill.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
