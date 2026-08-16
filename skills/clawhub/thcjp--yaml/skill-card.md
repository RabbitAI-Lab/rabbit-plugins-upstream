## Description:

YAML处理工具 helps agents write, check, parse, transform, and generate YAML that parses predictably across languages and versions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to create, validate, parse, convert, and troubleshoot YAML configuration files for cross-language workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares broad command and API capabilities that are not tightly scoped to YAML handling.

Mitigation: Review tool grants before installation, run the skill in a constrained agent environment, and require the publisher to remove or tightly scope unnecessary capabilities.

Risk: YAML workflows may involve local configuration files or sensitive operational data.

Mitigation: Limit file access to the intended workspace and review generated YAML before applying it to automation, deployment, or CI systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/yaml)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like responses with YAML snippets, configuration guidance, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or write local files and propose command execution when the host agent grants those tools.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
