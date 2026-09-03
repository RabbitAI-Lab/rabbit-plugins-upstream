## Description:

WorkBuddy安全稳定运行专家团（WB-SAFE） helps agents assess and improve WorkBuddy-style AI workspace security and stability across credentials, usage, connectivity, configuration, encryption, health, risk planning, and recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, developers, and operators use this skill to run structured security and stability checks for WorkBuddy-style agent workspaces, including credential hygiene, cost awareness, connector status, baseline drift, local health, and recovery readiness. It can produce triage reports, remediation guidance, local script commands, and configuration or recovery checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery actions can consume disk space or affect sandboxed recovery data when explicitly executed.

Mitigation: Run recovery in default dry-run mode first; use --execute only after confirming the sandbox path and available disk space.

Risk: Credential audits may locate sensitive files or secret-like patterns.

Mitigation: Report only file paths, line numbers, and categories; do not echo credential values into chat, logs, or reports.

Risk: Security remediation can involve sensitive changes such as deleting files, disconnecting connectors, or rotating production tokens.

Mitigation: Treat irreversible or credential-impacting changes as approval-gated actions and present the expected impact before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/wb-safe-team)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Eight Lines Defense](references/eight-lines-defense.md)
- [Safety Check SOP](references/safety-check-sop.md)
- [Scripts Guide](references/scripts-guide.md)
- [Security audit report](安全审计报告.md)
- [Security test results](security_results.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, structured checklists, local report files, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included local scripts are described as offline; audit output avoids secret values and recovery execution defaults to dry-run unless explicitly enabled.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
