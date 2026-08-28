## Description:

Guides project ideation via Socratic questioning to produce a validated brief before specification when requirements are unclear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product owners, and project teams use this skill to turn unclear project ideas into a structured project brief, compare approaches, capture rationale, and prepare for specification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project details may be saved locally and forwarded into downstream Attune workflow steps or subagents without a clear confirmation checkpoint.

Mitigation: Use non-confidential project information unless downstream skills have been reviewed, and inspect or remove .attune/brainstorm-session.json and docs/project-brief.md as needed.

Risk: Planning content may include business, customer, legal, security, or proprietary details.

Mitigation: Do not use this skill for sensitive planning unless the workspace, downstream workflows, and generated files are approved for that information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-brainstorming)
- [Attune homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown project brief, structured comparison tables, JSON session state, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save docs/project-brief.md and .attune/brainstorm-session.json; may pass project context to downstream Attune workflow steps and subagents.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
