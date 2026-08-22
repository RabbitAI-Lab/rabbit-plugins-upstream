## Description:

Skill Security Checker helps developers scan Skill directories for static security patterns, dependency risk, permission issues, optional sandbox behavior, and reportable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit WorkBuddy, ClawHub, or SkillHub skill directories before release, during third-party review, or in CI/CD quality gates. It produces scan findings, risk scores, and remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reads target skill directories and may include file paths, findings, or metadata in generated reports.

Mitigation: Run it only on projects you are authorized to inspect, review reports before sharing them, and direct output files to an approved location.

Risk: Optional supply-chain checks may perform external package or vulnerability lookups that can reveal dependency names from private projects.

Mitigation: Avoid --supply-chain on private projects unless external lookups are approved, or run in an offline/cache-only workflow.

Risk: Optional dynamic and syscall monitoring modes execute or observe target code and may require Docker, Windows Sandbox, root, or administrator privileges.

Mitigation: Enable --dynamic or --syscall-monitor only intentionally, prefer network-isolated sandbox settings, and review captured behavior before acting on findings.

Risk: Local cache and report files may persist after scans.

Mitigation: Use --skip-update for offline runs when appropriate and periodically review or clean local cache/report locations according to project data-handling rules.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/skill-security-checker)
- [Publisher Profile](https://clawhub.ai/user/fyniujin)
- [Scan Pattern Reference](references/scan-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, SARIF, shell commands, configuration, guidance]

**Output Format:** [Terminal text, Markdown guidance, JSON/HTML/SARIF reports, and CI configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report output may include risk scores, severity counts, findings, remediation suggestions, and optional CI quality-gate data.]

## Skill Version(s):

3.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
