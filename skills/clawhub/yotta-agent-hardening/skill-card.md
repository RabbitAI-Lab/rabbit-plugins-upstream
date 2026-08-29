## Description:

YuanSafe (元安全) scans an agent's own skills, MCP servers, tool descriptions, permissions, and data surfaces for prompt-injection, tool-boundary, and data-isolation hardening issues, then produces defensive reports and guardrails without attack payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to assess security exposure in agent runtimes they own or are authorized to inspect, including installed skills, MCP configuration, tool permissions, and data-handling surfaces. It helps produce hardening reports and reusable guardrails for defensive agent operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning overly broad or unauthorized directories can expose metadata about files and agent configuration.

Mitigation: Run scans only on directories the user owns or is authorized to inspect, and review scan targets before execution.

Risk: Default audit logging and generated reports may contain sensitive locations or risk metadata.

Mitigation: Review and redact reports or audit exports before sharing them outside the intended environment.

Risk: Global or multi-agent installation can make the skill available in more environments than intended.

Mitigation: Install only in agent environments where this hardening workflow is needed; avoid global installation unless multi-agent deployment is intended.

## Reference(s):

- [YuanSafe Tutorial](references/tutorial.md)
- [Detection Items](references/detection-items.md)
- [Report Template](references/report-template.md)
- [Guardrails Template](references/guardrails-template.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-agent-hardening)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Text, JSON, and Markdown reports with guardrail files and JSONL audit entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only target scans; audit metadata is written by default.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
