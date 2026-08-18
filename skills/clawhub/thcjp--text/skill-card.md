## Description:

用模式转换 helps agents transform, format, clean, localize, cite, and draft text using pattern-based instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and automation users use this skill to convert supplied content into cleaned, formatted, localized, cited, or writing-oriented text for agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and command authority without tight scoping or clear user controls.

Mitigation: Constrain the agent's permissions, keep invocations specific, and review file paths and commands before allowing execution.

Risk: Processing sensitive local files or text could expose data through agent output or follow-on actions.

Mitigation: Avoid sensitive files unless the workspace is permission-constrained and the resulting content is reviewed before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/text)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or JSON response containing processed text, status, and optional metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports content, mode, and style inputs; generated content should be reviewed before reuse.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
