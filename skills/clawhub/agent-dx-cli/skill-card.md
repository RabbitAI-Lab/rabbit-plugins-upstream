## Description:

Designs, reviews, and refactors CLIs for AI agents. Use when building Agent DX CLIs or checking existing CLI contracts. Checks predictability, defense in depth, and context efficiency with evidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, review, and refactor command-line interfaces for AI agents, preserving scope and authorization while assessing predictable contracts, safeguards, and context efficiency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Drive examples can initialize authentication and access resources during testing.

Mitigation: Use an isolated test environment and an account with resources intended for inspection; authorize implementation changes separately from review.

## Reference(s):

- [Principles, reasons, and examples](references/agent-dx-patterns.md)
- [GWS practice](references/gws.md)
- [Optional SKILL+CLI authoring](references/skill-cli.md)
- [GWS 0.22.5 source](https://github.com/googleworkspace/cli/tree/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/crates/google-workspace-cli/src)
- [GWS shared skill](https://github.com/googleworkspace/cli/blob/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/skills/gws-shared/SKILL.md)
- [GWS Drive skill](https://github.com/googleworkspace/cli/blob/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/skills/gws-drive/SKILL.md)
- [GWS Docs write skill](https://github.com/googleworkspace/cli/blob/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/skills/gws-docs-write/SKILL.md)
- [GWS share-doc-and-notify recipe](https://github.com/googleworkspace/cli/blob/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/skills/recipe-share-doc-and-notify/SKILL.md)
- [GWS persona-content-creator skill](https://github.com/googleworkspace/cli/blob/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/skills/persona-content-creator/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with evidence-based findings, scores, and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-scoped recommendations and verification evidence; no fixed output size is specified.]

## Skill Version(s):

0.4.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
