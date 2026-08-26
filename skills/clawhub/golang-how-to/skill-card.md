## Description:

Routes Go coding, review, debugging, setup, and configuration tasks to the relevant samber/cc-skills-golang skills and can configure project agent files to auto-load Go guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route Go coding, review, debugging, package lookup, refactoring, and project setup tasks to the most relevant Go skills. It also supports configuring project agent-instruction files so Go guidance loads consistently in supported agent harnesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configure and project-layout flows can persistently change project agent-instruction files so Go skills auto-load in future sessions.

Mitigation: Review the exact diff to CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules, or Copilot instructions before accepting those changes.

Risk: Some documented paths can write always-load directives without explicit confirmation.

Mitigation: Require explicit approval before running workflows that add or update always-load directives, especially in shared repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-how-to)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Golang skills catalog by category](references/by-category.md)
- [Competing clusters disambiguation](references/disambiguation.md)
- [Project configuration workflow](references/project-config.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Go, git, gopls, LSP, or gopls MCP tooling when the selected workflow requires local Go project inspection or navigation.]

## Skill Version(s):

1.4.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
