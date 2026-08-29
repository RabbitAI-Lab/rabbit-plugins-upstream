## Description:

Classifies and enforces constraints via soft vows, hard vows, and Nen Court layers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to classify project rules by enforcement strength, audit enforcement gaps, and decide when guidance should graduate to hooks or validator checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's broad governance and compliance triggers may activate in conversations where narrower project-rule guidance is expected.

Mitigation: Review activation behavior after installation and adjust trigger or routing policy if the skill appears outside intended enforcement-design workflows.

Risk: Recommendations about graduating rules to hooks or validators can block legitimate work if applied without context.

Mitigation: Review proposed hard vows or validator gates before deployment, test them in isolation or shadow mode, and keep human override paths for inconclusive cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-vow-enforcement)
- [claude-night-market imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with tables, protocols, example shell commands, and validator contract snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend hooks, validator checks, or human review for project-rule enforcement decisions.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
