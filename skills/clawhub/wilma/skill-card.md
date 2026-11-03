## Description:

Access Finland's Wilma school system from AI agents, for parents (and students with their own login). Fetch schedules, homework, exams, grades and the gradebook, lesson notes (merkinnät) and absence summaries, messages with replies, news, printouts and linked news resources — through the WilmAI MCP tools (`wilma_*`) when connected, or the wilma CLI. Start with a summary, drill into messages and news, and fetch linked attachments. Requires wilma-cli 2.0+.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and students use the skill to retrieve and understand school information from Wilma, including schedules, homework, grades, lesson notes, messages, and news. It can also fetch linked bulletin resources and school printouts.

### Deployment Geography for Use:

Finland

## Known Risks and Mitigations:

Risk: School records and saved login or MFA credentials are sensitive.

Mitigation: Use a trusted agent environment, keep secrets in the agent's secret settings, and never ask the user to enter a Wilma password in chat.

Risk: The skill runs an external CLI that may be installed or updated from npm; its credential storage protections were not audited in this bundle.

Mitigation: Use a trusted environment and follow the documented logout and credential removal steps when access should end.

## Reference(s):

- [WilmAI project on GitHub](https://github.com/aikarjal/wilmai)
- [WilmAI website](https://wilm.ai)
- [WilmAI Home](https://wilm.ai/home)
- [WilmAI CLI on npm](https://www.npmjs.com/package/@wilm-ai/wilma-cli)
- [Wilma skill on ClawHub](https://clawhub.ai/aikarjal/skills/wilma)

## Skill Output:

**Output Type(s):** [JSON, Text, Files, Guidance]

**Output Format:** [Structured JSON records, concise text or Markdown summaries, and downloaded documents when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are organized by student; requests can be narrowed by student and date.]

## Skill Version(s):

2.4.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
