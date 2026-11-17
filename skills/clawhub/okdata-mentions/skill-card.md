## Description:

Searches one page of posts for a chosen brand or keyword on selected social platforms and presents the results in a single table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can compare public brand or keyword mentions across selected social platforms. The skill gathers one page per selected platform and organizes post text, authors, timestamps, and engagement figures in a table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and related information are sent to the external okdata service.

Mitigation: Avoid sending confidential or personal information, and review whether the external service is appropriate for the query.

Risk: Each platform search is a paid call, so using several platforms or pages can increase charges.

Mitigation: State the planned calls and maximum cost before the first paid call, and get the user's go-ahead before more than six calls in one run.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-mentions)
- [okdata mentions documentation](https://okdata.online/skills/mentions/?src=skill-okdata-mentions)
- [okdata mentions documentation (Chinese)](https://okdata.online/zh/skills/mentions/?src=skill-okdata-mentions)
- [okdata agent setup guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Markdown table with a brief answer to the user's question]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One page per selected platform by default; includes post text, author, time, engagement figures, and source link when available.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
