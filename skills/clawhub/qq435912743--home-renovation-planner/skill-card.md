## Description:

Home Renovation Planner helps users estimate renovation budgets, plan project phases, compare materials and styles, review contract considerations, and prepare renovation acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning a home renovation use this skill to structure budgets, schedules, material choices, style options, avoidance checklists, contract review points, and final acceptance checks. It is best treated as planning guidance that should be checked against local requirements and professional advice for construction, contract, and safety decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a generic persistent learning system that can store user preferences, failure notes, and usage records beyond the immediate renovation guidance task.

Mitigation: Review the learner before installation, remove it or make it opt-in, and restrict any retained data to non-sensitive renovation metadata with clear deletion controls.

Risk: Renovation planning outputs may influence budgets, contracts, material purchases, or construction choices.

Mitigation: Use the skill as planning support and verify cost, contract, safety, and building-code decisions with qualified local professionals before acting.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with tables, checklists, examples, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a local learned_patterns.json memory file when the learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
