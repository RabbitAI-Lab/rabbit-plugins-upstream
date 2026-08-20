## Description:

Checks Markdown knowledge bases for broken links, missing frontmatter, tag inconsistencies, and cover metadata issues, with Chinese-language interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and knowledge-base owners use this skill to audit documentation projects for broken links, missing frontmatter, tag inconsistency, and cover metadata issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill overclaims security, compliance, and vulnerability assessment capabilities.

Mitigation: Use it as a Markdown knowledge-base health checker only; do not rely on it for real security, compliance, vulnerability assessment, or penetration testing.

Risk: The skill declares broad write, command execution, and API-oriented abilities without clear operational limits.

Mitigation: Require explicit approval before file writes, shell commands, or external API calls, and run it in a constrained workspace.

Risk: Auditing a project directory may expose private documentation or repository contents to the active agent.

Mitigation: Run it only on directories the operator is comfortable exposing to the agent and remove sensitive material before review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/solo-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON audit reports with fix guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include issue summaries, scores, detailed findings, and improvement suggestions.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.4.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
