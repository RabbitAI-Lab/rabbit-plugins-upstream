## Description:

记忆雷达 is a Chinese-language agent skill that guides security scans of AI agent memory files for prompt injection, credential leakage, cross-file threat correlation, false-positive suppression, and quarantine or recovery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and agent operators use this skill to review AI agent memory files, imported external content, and workspace configuration for prompt injection, credential leakage, data exfiltration instructions, and related memory-security risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence notes missing referenced scripts and overbroad wording, so runtime behavior may not be fully represented by the artifact text.

Mitigation: Review the referenced scripts or implementation before enabling scheduled monitoring, quarantine, or recovery actions.

Risk: Optional remote LLM analysis may send redacted memory content outside the local environment.

Mitigation: Use local scanning by default and enable --allow-remote only when redacted remote analysis is acceptable.

Risk: Quarantine and recovery workflows can modify memory files after user confirmation.

Mitigation: Confirm the files and lines to be changed, verify backups exist, and review proposed changes before quarantine.

Risk: Pattern-based local scanning can miss semantic prompt injection or credentials without known prefixes.

Mitigation: Treat scan results as review guidance and use additional analysis for high-risk imported memory or nonstandard secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memory-radar)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples and an optional JSON scan-report structure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language workflow; local scanning by default, with optional remote LLM analysis only when enabled by the user.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
