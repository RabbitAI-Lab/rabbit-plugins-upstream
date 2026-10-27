## Description:

Access Finland's Wilma school system from AI agents. Fetch schedules, homework, exams, grades and the gradebook, lesson notes (merkinnät) and absence summaries, messages with replies, news, printouts and linked news resources — through the WilmAI MCP tools (`wilma_*`) when connected, or the wilma CLI. Start with a summary, drill into messages and news, and fetch linked attachments. Requires wilma-cli 2.0+.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and guardians use this skill through an AI agent to review a child's schedules, homework, exams, grades, lesson notes, messages, school news, and available printouts in Wilma. It can also summarize relevant items and retrieve bulletin attachments.

### Deployment Geography for Use:

Finland

## Known Risks and Mitigations:

Risk: Wilma data can include sensitive children's school records, and the CLI saves login credentials locally.

Mitigation: Use an agent environment and AI provider trusted with school records and saved credentials; narrow requests to one child when appropriate.

Risk: A saved MFA setup secret or an unreviewed CLI update could expose account access or data.

Mitigation: Protect saved MFA setup secrets and consider installing a reviewed CLI version. Remember that logout ends the Wilma session but retains the saved login.

## Reference(s):

- [WilmAI GitHub repository (linked in the skill documentation)](https://github.com/aikarjal/wilmai)
- [WilmAI website](https://wilm.ai)
- [WilmAI Home](https://wilm.ai/home)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Files, Guidance]

**Output Format:** [Wilma data in JSON, with concise text or Markdown summaries and retrieved attachments where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results cover all connected children by default and can be narrowed to one child; available data and attachments vary by school and account.]

## Skill Version(s):

2.3.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
