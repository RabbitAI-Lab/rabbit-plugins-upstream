## Description:

Analyzes agent conversation records or context inventories to estimate token usage, identify context pollution and compaction risks, and suggest ways to preserve or reduce material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to understand how a conversation's context budget is distributed, investigate forgotten constraints or other context-pollution symptoms, and decide what to retain, structure, reference, or discard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation records may contain secrets or other sensitive information, and report redaction does not prevent the model from receiving the original input.

Mitigation: Share only records intended for analysis and remove secrets before providing them to the agent.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/z-zihan/skills/context-budget-analyzer)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with estimated token breakdown, context-pollution findings, compaction risks, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token counts are estimates; when no context-window size is provided, the skill uses a 200k-token assumption and labels it.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
