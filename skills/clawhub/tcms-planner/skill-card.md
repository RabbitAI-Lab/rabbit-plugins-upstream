## Description:

Content topic-planning agent that generates structured topic briefs from knowledge-base updates, competitor signals, the content calendar, and performance data, without creating article body content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Brand-side content marketing teams use this skill to turn product knowledge-base updates, competitor signals, and content calendars into one to three prioritized topic briefs. It supports planning and handoff to downstream writing workflows while requiring human confirmation before content creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad content-planning trigger phrases may invoke the skill in general editorial conversations.

Mitigation: Use it in workspaces where reading calendars, knowledge-base sections, and content inventories for brief generation is acceptable.

Risk: Topic briefs may reference internal customer cases or insufficient source material.

Mitigation: Require human confirmation before downstream writing, mark internal cases for redaction, and decline recommendations when supporting material is too thin.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown topic brief with an execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes briefs to content-calendar/briefs/YYYY-MM-DD-brief.md and requires human confirmation before downstream content-writing use.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
