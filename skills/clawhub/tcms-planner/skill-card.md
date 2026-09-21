## Description:

Content topic-planning agent that generates structured topic briefs from knowledge-base updates, competitor signals, the content calendar, and performance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams for technology products use this skill to turn knowledge-base updates, competitor signals, content calendars, and performance data into prioritized topic briefs. It is intended for topic planning only, not article drafting or calendar approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads project planning materials and may access sensitive marketing context in shared repositories.

Mitigation: Confirm which project files it may read before use and scope access to the relevant content calendar, knowledge-base, and published-content inventory.

Risk: Topic briefs may be used as inputs to downstream content-writing work without review.

Mitigation: Require human confirmation before handing a brief to downstream writing or publishing skills.

Risk: Brief files could be written outside the intended planning area if project paths are misconfigured.

Mitigation: Limit brief creation to the documented content-calendar/briefs path and review path configuration in shared repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-planner)
- [README.md](artifact/README.md)
- [README_zh.md](artifact/README_zh.md)

## Skill Output:

**Output Type(s):** [markdown, text, guidance]

**Output Format:** [Markdown topic brief plus execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes brief files under content-calendar/briefs/YYYY-MM-DD-brief.md when project inputs are available; requires human confirmation before downstream writing.]

## Skill Version(s):

1.1.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
