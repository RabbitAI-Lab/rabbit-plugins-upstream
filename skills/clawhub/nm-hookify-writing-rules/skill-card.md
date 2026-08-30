## Description:

Creates behavioral rules in markdown to block dangerous commands or restrict AI behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to define persistent local guardrail rules that warn on or block risky commands, file edits, prompts, or stop events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad or incorrect block rule can interfere with normal agent work or command execution.

Mitigation: Review each generated .claude/hookify.*.local.md rule before enabling it, test the pattern, and start with warning rules when practical.

Risk: Persistent local guardrail rules may continue affecting future sessions after the original task is complete.

Mitigation: Name rules descriptively, document their intent, and disable or delete rules that are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-hookify-writing-rules)
- [Hookify Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/hookify)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with YAML frontmatter examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Hookify rule guidance for .claude/hookify.*.local.md files; review generated rules before enabling.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
