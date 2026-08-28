## Description:

元审 yotta-vetter helps agents and users perform a structured pre-install security review of other skills using a four-phase checklist, lightweight rule scanning, optional GitHub source metadata checks, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and security reviewers use this skill before installing or accepting an unknown agent skill to inspect source, code, permissions, and risk, then produce a traceable vetting report. It supports human review rather than making final installation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pre-install review reports can miss issues or produce false positives.

Mitigation: Treat the report as an initial review aid, require human confirmation before installation, and run deeper security scanning when high or critical findings appear.

Risk: The source check contacts GitHub and caches repository metadata locally.

Mitigation: Use source checks only for repositories the reviewer intends to inspect, and rely on the local check mode when offline or when network access is not desired.

Risk: Global installation can copy the skill into many agent skill directories.

Mitigation: Prefer --dir or a specific agent target for least-scope installation; use -g only when installation across all known agent directories is intended.

## Reference(s):

- [Four-phase skill review checklist](references/checklist.md)
- [SKILL VETTING REPORT template](references/vetting-report-template.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-vetter)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text reports, optional JSON, Markdown report files, and follow-up shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes summarize the highest detected severity: 0 for clean or low, 1 for medium, 2 for high, 3 for critical, and 4 for errors.]

## Skill Version(s):

0.1.4 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
