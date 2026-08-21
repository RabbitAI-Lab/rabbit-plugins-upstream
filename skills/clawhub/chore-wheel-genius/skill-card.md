## Description:

Smart chore assignment for families and households that assigns tasks based on skills, schedule, and fairness scoring while tracking chore history, rotating unpleasant tasks, and generating chore charts and fairness reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Households and family organizers use this skill to set up chore members and tasks, generate effort-weighted assignments, track completions, and review fairness over time. Agents can use it to provide command-line chore planning guidance and produce household chore reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores household members, ages, skills, assignments, and completion history in ~/.chore_wheel.json.

Mitigation: Review the local data file location before use, avoid entering sensitive household details beyond what is needed, and delete ~/.chore_wheel.json when the history should be reset or removed.

Risk: Age-based chore suggestions may be mistaken for safety approval for tasks involving cooking, chemicals, tools, yard equipment, repairs, or babysitting.

Mitigation: Treat age guidance as rough planning input and require adult judgment or supervision for any chore with safety implications.

## Reference(s):

- [Fairness Algorithm](references/fairness-algorithm.md)
- [Age-Appropriate Chores](references/age-chores.md)
- [Server-resolved source repository](https://github.com/voronindenis5/chore-wheel-genius)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/chore-wheel-genius)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local CLI guidance, chore assignment output, visual text charts, fairness summaries, and multi-week reports.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
