## Description:

YuanSafe yotta-agent-hardening statically scans an AI agent runtime across prompt-injection defense, tool-call boundaries, and data isolation, then produces hardening reports and enforceable guardrails without attack payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to assess agent runtimes they own or are authorized to inspect, prioritize hardening work, and generate defensive guardrails for ongoing operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local scans can inspect sensitive directories when a user points the skill at overly large or sensitive targets.

Mitigation: Install into a controlled skills directory and scan only directories the user owns or is authorized to inspect.

Risk: Audit metadata is written locally by default, which may reveal what was scanned and what severity was observed.

Mitigation: Before scanning sensitive projects, use --config-dir or YOTTA_HARDENING_DIR to direct audit logs to an appropriate local location.

## Reference(s):

- [Detection Items](references/detection-items.md)
- [Guardrails Template](references/guardrails-template.md)
- [Report Template](references/report-template.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Terminal text, JSON, Markdown reports, and Markdown guardrails.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only scans; writes a local audit log by default and optional report or guardrail files when requested.]

## Skill Version(s):

0.2.4 (source: frontmatter, package.json, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
