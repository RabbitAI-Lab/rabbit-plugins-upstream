## Description:

Comprehensively scope, enumerate, test, validate, and report security findings with specialized roles for thorough bug bounty assessments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Security engineers and bug bounty practitioners use this agent configuration bundle to scope authorized targets, enumerate attack surface, test hypotheses, validate findings, and draft triage-ready reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can be used outside authorized testing scope or against unintended targets.

Mitigation: Install only for authorized security testing and confirm target scope before use.

Risk: Security testing may expose secrets or sensitive client data in the workspace or agent memory.

Mitigation: Run in a contained workspace and avoid storing secrets or sensitive client data in memory unless intended for the engagement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/bug-bounty-team)
- [Source skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports with structured findings and inline commands or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain within the confirmed engagement scope and be reviewed before submission.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
