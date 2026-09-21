## Description:

Detects malicious patterns in AI skills and scans Windows/Linux system security baselines with a read-only, zero-dependency security audit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to scan agent skill directories before installation, audit installed skills, and check local Windows/Linux security baselines while keeping outputs read-only and masked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: System scans may inspect sensitive local security configuration when permissions allow.

Mitigation: Run system scans only on machines you administer, expect read-only inspection, and review masked reports before sharing them.

Risk: Bulk installation can copy the skill into many agent directories.

Mitigation: Prefer installing to a specific agent or directory and use targeted --path scans where possible.

Risk: Some detector hits are context-dependent and may require human review.

Mitigation: Treat findings as audit signals, verify high-risk locations manually, and obtain user confirmation before any remediation outside the skill.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-security-audit)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Threat patterns](references/threat-patterns.md)
- [Risk remediation guide](references/remediation-guide.md)
- [System baseline checks](references/system-baseline.md)
- [NPM package](https://www.npmjs.com/package/@yottameta/yotta-security-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text reports with optional JSON and Markdown report files, plus command-line guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are read-only and masked by default; exit codes indicate highest detected severity.]

## Skill Version(s):

0.2.4 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG released 2026-09-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
