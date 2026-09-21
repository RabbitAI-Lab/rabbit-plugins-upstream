## Description:

Generates a daily morning briefing by searching current news, summarizing selected items, writing a Markdown briefing, and sending it to a CEO recipient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and executive-support teams can use this skill to assemble a daily briefing from current news and send it to an executive recipient. Review the generated briefing and recipient configuration before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically send a generated briefing file to a hard-coded CEO recipient.

Mitigation: Use only where that recipient is explicitly approved, or revise the skill to make recipients configurable and require human approval before sending.

Risk: The Python implementation invokes OpenClaw tools through shell command execution.

Mitigation: Prefer scoped tool APIs or run the skill in a constrained environment after reviewing the exact commands it can execute.

Risk: Briefing content depends on live web search results and may include stale, irrelevant, or misleading snippets.

Mitigation: Review the generated briefing before forwarding it or using it for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/daily-morning-meeting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown briefing file with message notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a dated local briefing file and may send that file as message media.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
