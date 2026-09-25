## Description:

JSON转YAML工具 converts JSON data into YAML through an Expanso Edge pipeline, with Chinese-language guidance for configuration and workflow use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to convert JSON data into YAML for API integration, configuration, and workflow handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broader API, file, command-execution, and credential-related authority than its JSON-to-YAML purpose explains.

Mitigation: Install only when that broader workflow is intentional, and constrain the data, files, credentials, APIs, and commands the agent may access.

Risk: Command and file operations could affect local files or run unintended actions if accepted without review.

Mitigation: Review proposed commands and file writes before execution, and prefer local-only JSON parsing for routine conversions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/expanso-json-to-yaml)
- [SkillHub skill page](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Code, Configuration, Guidance]

**Output Format:** [YAML text with Markdown guidance and JSON status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution logs and setup commands; review requested actions before granting file, credential, API, or command access.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
