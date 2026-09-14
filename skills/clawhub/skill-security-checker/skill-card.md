## Description:

Skill 安全审计扫描器 helps agents audit skill directories for static security issues, dependency vulnerabilities, permission risks, sandbox behavior, supply-chain signals, and CI/CD reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and release engineers use this skill to check ClawHub, WorkBuddy, or SkillHub skill directories before release, review third-party skills, and generate scan reports for local or CI quality gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security verdict is suspicious because some safeguards may read outside the selected scan folder or provide more network access and assurance than expected.

Mitigation: Review before installing, scan only directories intentionally selected, and avoid untrusted archives that preserve symlinks until scan-root containment is fixed.

Risk: Update checks, OSV refreshes, supply-chain lookups, and dynamic allow-domain settings may initiate network access.

Mitigation: Use --skip-update in private or offline environments and enable refresh or allow-domain options only when network access is approved.

Risk: Dynamic scanning isolation and behavior capture vary by backend, and evidence warns not to rely on Windows Sandbox or allow-domain behavior for strong isolation guarantees.

Mitigation: Treat dynamic scan results as advisory, prefer a locked-down Docker run with no network for higher isolation, and review any sandbox configuration before executing untrusted skills.

## Reference(s):

- [Scan Patterns Reference](references/scan-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/skill-security-checker)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands plus text, JSON, HTML, or SARIF scan reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write report files when an output path is supplied; exit codes indicate whether findings are low, medium, high, or critical.]

## Skill Version(s):

3.4.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
