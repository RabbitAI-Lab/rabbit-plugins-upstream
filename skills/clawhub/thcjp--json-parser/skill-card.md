## Description:

JSON解析器 helps agents parse and validate construction API, IoT sensor, and BIM JSON data and convert results into tabular outputs for analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and automation teams use this skill to inspect JSON from construction APIs, IoT sensors, and BIM metadata, validate structure, flatten records, and prepare tables for reports or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution, file writing, and API-related authority without enough scoping for a parser-style skill.

Mitigation: Enable it only in environments where command execution and file writing are acceptable, review proposed commands before execution, and restrict permissions to the files and tools needed for the current JSON parsing task.

Risk: JSON inputs, parsed outputs, or API-key configuration may expose private data if broad workspace or credential access is granted.

Mitigation: Avoid providing sensitive API keys or private data unless necessary, use environment variables for required secrets, and remove secrets or sensitive fields from logs and generated outputs.

Risk: The security verdict is suspicious because the documented authorities are broader than the parser use case requires.

Mitigation: Review the skill carefully before installation and prefer a sandboxed agent session for untrusted or third-party data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-parser)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce parsing guidance, validation results, flattened JSON structures, table-ready data, and environment configuration steps depending on agent permissions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
