## Description:

Browse hookify rule catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to browse Hookify rules by category and install pre-built project rules before writing custom rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing rules can create persistent project-local .claude/hookify.*.local.md files.

Mitigation: Review generated .claude/hookify.*.local.md files before relying on the installed rules.

Risk: Bulk install commands may add Hookify rules beyond the single rule the user intended.

Mitigation: Run bulk install commands only in the repository where persistent Hookify rules are wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-hookify-rule-catalog)
- [Hookify homepage](https://github.com/athola/claude-night-market/tree/master/plugins/hookify)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to create project-local .claude/hookify.*.local.md rule files when installing rules.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
