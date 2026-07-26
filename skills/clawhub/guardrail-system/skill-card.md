## Description: <br>
Guardrail System provides input, tool-use, and output guardrails for AI agents, including prompt-injection checks, permission-tier checks, and sensitive-information redaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add lightweight local checks around user input, tool calls, and assistant output. It is intended to help detect common prompt-injection patterns, require confirmation or authorization for higher-risk tools, and redact common sensitive strings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Regex-based guardrails may miss prompt-injection or sensitive-data patterns outside the included examples. <br>
Mitigation: Review and tune the injection and redaction patterns for the target application before relying on the skill for production security decisions. <br>
Risk: Tool permissions are based on configured tool names, so an incomplete or outdated tool list can lead to incorrect confirmation or authorization behavior. <br>
Mitigation: Map all available tools to the intended permission tier and review unknown-tool handling during integration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/guardrail-system) <br>
- [Injection Patterns](artifact/references/injection_patterns.md) <br>
- [Permission Levels](artifact/references/permission_levels.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Configuration, Guidance, Text] <br>
**Output Format:** [Python API results and sanitized text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns structured guardrail results with allow/deny status, confirmation or authorization flags, reasons, messages, and optional sanitized output.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
