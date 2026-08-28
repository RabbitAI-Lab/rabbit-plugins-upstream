## Description:

Provides anti-hallucination guardrails for summary tasks so agents report empty or partial source records instead of fabricating blank-day activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to make scheduled or user-requested summary workflows trace each factual item to current-session logs or tool results and return "no records" when sources are empty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Summary workflows can fabricate activity when logs or tool results are empty.

Mitigation: Require summaries to return "no records" when current-session sources are empty.

Risk: User profiles or long-term memory can be mistaken for evidence of dated activity.

Mitigation: Require each dated factual item to trace to a current-session conversation segment or tool result.

Risk: Unsupported summary details can become false evidence if written to persistent records.

Mitigation: Gate persistence on per-item source checks and omit or mark any item whose source is unverified.

## Reference(s):

- [Grounded Summaries skill page](https://clawhub.ai/mowenqwq/skills/grounded-summaries)
- [Publisher profile](https://clawhub.ai/user/mowenqwq)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown guidance and checklist text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static guidance; no tools, code execution, or credential access requested.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
