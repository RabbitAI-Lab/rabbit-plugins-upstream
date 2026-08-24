## Description:

Content topic-planning agent that generates structured topic briefs from knowledge-base updates, competitor signals, the content calendar, and performance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketers, product marketing teams, and editorial planners use this skill to turn calendar needs, knowledge-base updates, competitor signals, and performance data into structured topic briefs for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads configured content-planning sources and writes dated brief files, which may expose or modify planning material in inappropriate workspaces.

Mitigation: Install and run it only in workspaces where content calendar, knowledge-base, and brief-file access is appropriate.

Risk: Generated topic briefs may contain incomplete, stale, or unsuitable planning guidance.

Mitigation: Review generated briefs before passing them to writing, approval, or publishing workflows.

Risk: Broad routing terms may activate the skill for requests that are not intended to create a topic-selection brief.

Mitigation: Confirm the trigger source and route before producing or saving a brief.

## Reference(s):

- [tcms-planner ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-planner)
- [haiyangchenbj ClawHub publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown topic brief file with an execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes dated briefs under content-calendar/briefs/ and requires human confirmation before downstream content writing.]

## Skill Version(s):

1.1.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
