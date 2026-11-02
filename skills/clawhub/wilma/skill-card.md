## Description:

Access Finland's Wilma school system from AI agents, for parents (and students with their own login). Fetch schedules, homework, exams, grades and the gradebook, lesson notes (merkinnät) and absence summaries, messages with replies, news, printouts and linked news resources — through the WilmAI MCP tools (`wilma_*`) when connected, or the wilma CLI. Start with a summary, drill into messages and news, and fetch linked attachments. Requires wilma-cli 2.0+.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and students with their own Wilma login use the skill to review schedules, homework, exams, grades, lesson notes, absences, messages, school news, and printouts. It helps prepare concise, actionable school updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration handles children’s private school records and may retain passwords and authenticator setup keys.

Mitigation: Use a trusted computer or agent environment for login and access. Select a student when narrower results are appropriate.

Risk: Logging out ends the session but leaves the saved login, and the externally maintained CLI’s implementation and credential-storage protections were not verified in this review.

Mitigation: Remove saved accounts separately when you want to delete stored logins, and review and trust the CLI source before installing or updating it.

## Reference(s):

- [WilmAI project repository](https://github.com/aikarjal/wilmai)
- [WilmAI website](https://wilm.ai)
- [Wilma skill release on ClawHub](https://clawhub.ai/aikarjal/skills/wilma)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Concise structured text summaries of school records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include relevant dates and item IDs.]

## Skill Version(s):

2.3.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
