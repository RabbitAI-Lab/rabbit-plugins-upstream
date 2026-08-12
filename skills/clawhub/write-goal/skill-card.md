## Description:

Helps an agent turn a rough user intention into a structured, verifiable goal with an objective, completion criterion, boundaries, and optional budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to refine vague or broad requests into completion contracts before autonomous execution. It is most useful when the user wants help writing, setting, or improving a goal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A poorly reviewed goal can commit an agent to the wrong objective, completion criterion, boundary, or budget.

Mitigation: Review the structured goal before accepting it or replacing an active goal.

Risk: Goal-management tools, when available, can turn drafted text into an active execution target.

Mitigation: Confirm the objective, stop rule, and any explicit budget before allowing the goal to be committed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/write-goal)
- [Publisher profile](https://clawhub.ai/user/wlykan)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include objective, completion criterion, boundary, and budget sections.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
