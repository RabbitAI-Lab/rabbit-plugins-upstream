## Description:

Figma设计工具v2 helps an agent browse Figma teams, projects, files, pages, and nodes; export images; manage comments; inspect version history, components, styles, and design variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and workflow automation users can use this skill to inspect and automate Figma workspace operations, including design-file browsing, image export, comments, version history, components, styles, and design variables. It is not a replacement for human creative judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill asks for broad local read, write, and command execution authority without tight scoping.

Mitigation: Review carefully before installing; keep local command execution and file writes disabled or sandboxed unless explicitly needed.

Risk: Figma workspace access may expose sensitive team files or design assets.

Mitigation: Use a least-privileged Figma token or account and avoid exposing sensitive team files unless required for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/figma-2)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and shell configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Figma operation results, file metadata, image export links, comments, version information, component/style data, or design-variable information.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
