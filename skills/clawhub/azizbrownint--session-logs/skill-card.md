## Description:

Search and analyze your own session logs (older/parent conversations) using jq.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to locate and analyze prior session logs when a user asks about historical context, earlier conversations, message counts, tool usage, or cost summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to search broad conversation history, including reset or deleted transcript archives.

Mitigation: Limit searches to specific sessions, dates, or phrases, and require explicit confirmation before reading reset or deleted transcript archives.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/session-logs)
- [ClawHub publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires jq and rg; outputs are intended to be scoped to local session-log searches and summaries.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
