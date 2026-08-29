## Description:

Extracts writing style patterns from exemplar text into a reusable profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and agents use this skill to analyze exemplar text, extract measurable style features, select representative passages, and generate a reusable style profile for consistent downstream writing or editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Style profiles may retain excerpts from exemplar documents.

Mitigation: Use only source text that may be reused or quoted, and review generated profiles before sharing or publishing them.

Risk: Broad style-related triggers may surface the skill for general writing requests.

Mitigation: Confirm that the user wants style-profile extraction or style-guided writing before applying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-style-learner)
- [Publisher profile](https://clawhub.ai/user/athola)
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and YAML-style profile guidance with inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reusable style profiles with quantitative metrics, exemplar passages, anti-patterns, and validation guidance.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
