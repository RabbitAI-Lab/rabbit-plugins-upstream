## Description:

Creates, inspects, processes, and optimizes image files and visual assets, with support for format selection and agent-guided image-processing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and teams use this skill to guide image asset creation, inspection, processing, optimization, and format selection in agent workflows. It is not intended for complex decisions that require independent human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image workflows may involve sensitive local image assets.

Mitigation: Avoid providing sensitive images unless necessary, and confirm that the agent only reads or writes image assets needed for the task.

Risk: Image-related shell commands can affect local files when executed by the agent.

Mitigation: Require user confirmation for shell commands outside a clear image-processing workflow.

Risk: API keys or credentials could be exposed if embedded in prompts, files, or logs.

Mitigation: Keep API keys in environment variables and avoid committing or sharing credential values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/image)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON response examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write image assets and produce execution logs; outputs depend on the requested image workflow and agent platform.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
