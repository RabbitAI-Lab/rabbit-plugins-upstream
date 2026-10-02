## Description:

Read MaxPreps high school sports data to find US schools, teams, schedules, scores, rosters, rankings, statistics, and athlete careers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public US high school sports schedules, scores, team records, rosters, rankings, statistics, and athlete histories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the included helper makes network requests to MaxPreps and writes a small temporary cache.

Mitigation: Review the helper before execution and allow only the read-only MaxPreps access needed for the task.

Risk: Public roster and athlete information may identify students.

Mitigation: Use athlete details only when necessary and avoid unnecessary bulk collection.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/maxpreps-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with example shell commands and structured sports data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers draw on public MaxPreps pages; current-season records may be empty before play begins.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
