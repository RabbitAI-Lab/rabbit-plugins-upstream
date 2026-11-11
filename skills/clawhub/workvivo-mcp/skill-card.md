## Description:

This skill helps users read and search their organization's Workvivo intranet for company updates, events, people, spaces, and documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can use the skill to find and read company news, feed updates, events, colleagues, spaces, and linked documents in their signed-in Workvivo account. It requires the user's signed-in browser session and returns read-only information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic triggers may cause searches through the user's authenticated Workvivo access for unrelated requests, and those searches are recorded in Workvivo history.

Mitigation: Use the skill only when the request clearly concerns Workvivo, and account for the query being saved before searching.

Risk: The security scan was partial because a referenced document was missing, so its evidence is incomplete.

Mitigation: Review the missing referenced document and reassess the skill before relying on the scan as complete.

## Reference(s):

- [Workvivo MCP on ClawHub](https://clawhub.ai/chrischall/skills/workvivo-mcp)
- [Publisher profile: chrischall](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text summaries and Markdown content from Workvivo]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; times are returned in UTC; Workvivo search queries are recorded in the user's search history.]

## Skill Version(s):

0.4.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
