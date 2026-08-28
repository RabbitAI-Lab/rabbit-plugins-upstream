## Description:

Build composable skill modules with hub-and-spoke loading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design, refactor, and troubleshoot modular agent skills that keep core guidance concise while loading deeper modules only when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may cause the skill to be invoked during general architecture or token-budget conversations.

Mitigation: Confirm that the task involves modular skill design, refactoring, or token-efficiency planning before applying detailed module guidance.

Risk: The artifact references external tools and plugins that are separate software from the documentation-only skill.

Mitigation: Review and scan any referenced external tool or plugin before running or installing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-modular-skills)
- [metadata.openclaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [artifact/SKILL.md](artifact/SKILL.md)
- [Core workflow module](artifact/modules/core-workflow.md)
- [Optimization techniques module](artifact/modules/optimization-techniques.md)
- [Troubleshooting module](artifact/modules/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with example shell commands and structured frontmatter snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no hidden execution, persistence, or sensitive data access found in security evidence.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
