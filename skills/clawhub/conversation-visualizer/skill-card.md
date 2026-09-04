## Description:

Generate visual HTML summaries from OpenClaw session history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn OpenClaw conversation history into shareable visual summaries after chats, planning sessions, or decision discussions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read session history and create visual exports that may contain sensitive conversation content.

Mitigation: Use it only with conversations that are appropriate to summarize, summarize sensitive content generically or ask first, and review generated files before sharing.

Risk: The skill requests an unexplained skill-management capability.

Mitigation: Remove or justify the skill_workshop permission before deployment and review the installation against least-privilege expectations.

Risk: Generated files may be written to the workspace or another user-selected output directory.

Mitigation: Confirm the output location and inspect generated HTML, Markdown, PNG, and PowerPoint files before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/conversation-visualizer)
- [Project homepage](https://github.com/openclaw/skills/conversation-visualizer)
- [Publisher profile](https://clawhub.ai/user/monaxamo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Self-contained HTML, Markdown summary, PNG screenshots, PowerPoint deck, and output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local session history and local model summarization; generated artifacts should be reviewed before sharing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
