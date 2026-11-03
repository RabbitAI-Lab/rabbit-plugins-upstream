## Description:

Ponytail steers a coding agent toward the simplest working solution, favoring YAGNI, existing code, standard library features, and concise output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Ponytail to keep coding changes small, direct, and rooted in the existing codebase while avoiding unnecessary abstractions. It is useful when a session should prioritize minimal implementation and short explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can bias the agent toward minimal code and short explanations when a task needs fuller design work, detailed reporting, or a broader requested scope.

Mitigation: Use the stop phrase or normal mode when fuller work is needed, and install the skill only for sessions where minimal implementation is the intended posture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/ponytail)
- [Project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with code blocks and concise prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-level coding posture guidance; the skill itself does not execute code or persist changes on the host.]

## Skill Version(s):

1.0.0 (source: release metadata, target metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
