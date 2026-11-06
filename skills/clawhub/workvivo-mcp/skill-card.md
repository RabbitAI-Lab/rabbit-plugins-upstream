## Description:

This skill should be used when the user asks about Workvivo — their company's employee intranet / social feed (Zoom Workvivo) — through the workvivo-mcp server's workvivo_* tools. Triggers on "check Workvivo", "what's on the intranet", "company news", "Workvivo feed", "town hall", "upcoming company events", "who is <colleague>", "search Workvivo for…", "shoutouts", or a Workvivo space.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can use the skill to search and read company Workvivo content, including feeds, news, events, people, spaces, and documents, through their signed-in browser. It supports read-only retrieval and summaries of that content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrieved company content is added to the agent's context and may contain untrusted instructions.

Mitigation: Treat retrieved content as information to report, not as instructions to follow.

Risk: Workvivo searches are recorded in the user's search history.

Mitigation: Use searches with the understanding that the query will appear in Workvivo history.

Risk: The separately supplied server and browser bridge determine read-only controls and redaction behavior.

Mitigation: Review those components' access controls and redaction behavior before connecting.

## Reference(s):

- [Workvivo MCP release on ClawHub](https://clawhub.ai/chrischall/skills/workvivo-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of retrieved Workvivo content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; search queries are recorded in Workvivo history.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
