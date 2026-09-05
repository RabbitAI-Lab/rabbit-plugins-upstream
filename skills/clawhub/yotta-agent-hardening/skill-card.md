## Description:

YuanSafe is a defensive AI-agent hardening skill that statically scans an agent runtime's installed skills, MCP servers, tool descriptions, permissions, and data surfaces across prompt-injection defense, tool-call boundaries, and data isolation, then produces hardening reports and enforceable guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and agent operators use this skill to check agent or skill environments they own or are authorized to inspect for prompt-injection exposure, over-broad tool permissions, and data-isolation risks. It helps establish a hardening baseline, generate defensive guardrails, and review audit trails without producing attack payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reads text files under the target path and may inspect sensitive configuration locations.

Mitigation: Run it only on directories and configurations you own or are authorized to inspect, and prefer a narrow explicit target over broad or global scans.

Risk: The skill writes local audit logs and can write optional guardrail or report files.

Mitigation: Choose intentional output locations, review generated reports and audit exports before sharing them, and account for the default audit trail in local data-handling practices.

Risk: Hardening recommendations can be incomplete or require context-specific judgment.

Mitigation: Treat reports and guardrails as defensive review inputs, then have a qualified reviewer confirm remediation priorities before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-agent-hardening)
- [Detection items](references/detection-items.md)
- [Guardrails template](references/guardrails-template.md)
- [Report template](references/report-template.md)
- [Chinese tutorial](references/tutorial.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-agent-hardening)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Terminal text, JSON, Markdown reports, Markdown guardrails, JSONL audit logs, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use class-level descriptions and avoid copy-paste injection strings or credential values.]

## Skill Version(s):

0.2.5 (source: server release evidence; artifact frontmatter, package.json, and changelog report 0.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
