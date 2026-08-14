## Description:

Consolidate helps agents gather AI PR reviews, classify findings by type and severity, post an AI Review Summary and Formal Review, and register deferred items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to consolidate CodeRabbit, Copilot, and internal review feedback on pull requests or issues, decide which findings are valid, publish review outcomes, and track deferred follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish GitHub reviews, request changes, edit PR descriptions, and write tracking records without consistent per-action confirmation.

Mitigation: Invoke it explicitly with interactive review enabled and use it only on repositories and pull requests where automated review actions are acceptable.

Risk: Included hook scripts can block non-consolidate review comments if registered.

Mitigation: Inspect the hook scripts before registration and enable them only when that enforcement behavior is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill workflow](SKILL.md)
- [PR workflow](pr.md)
- [Posting workflow](post.md)
- [Superpowers dependency](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review summaries, formal review bodies, tracking notes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish GitHub comments or reviews and update PR descriptions when invoked with appropriate repository credentials.]

## Skill Version(s):

0.5.3 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
