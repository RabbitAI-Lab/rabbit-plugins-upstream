## Description:

Audits a user-selected Git repository for maintainability, configuration problems, dependency risks, accidental secret exposure, and CI/CD weaknesses, producing an evidence-based report without modifying files by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and security reviewers use this skill to triage a selected repository before release or handoff and prioritize evidence-backed maintenance and security findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository inspection may encounter credentials or other sensitive content.

Mitigation: Inspect only the repository the user selects and redact any suspected secrets in the report.

Risk: Follow-up checks or fixes may run code, change files, or transmit repository content.

Mitigation: Keep the initial review read-only and obtain explicit approval for each action with side effects.

Risk: Static findings may be mistaken for confirmed vulnerabilities.

Mitigation: Distinguish observed evidence from likely risks and checks requiring manual validation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hmahmadcs/skills/git-repository-health-auditor)
- [Publisher profile](https://clawhub.ai/user/hmahmadcs)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked findings, scope and limitations, prioritized actions, and open questions; secret values are redacted.]

## Skill Version(s):

1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
