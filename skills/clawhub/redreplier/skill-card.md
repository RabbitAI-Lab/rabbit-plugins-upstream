## Description:

Helps agents monitor and triage AI-scored mentions of a product or website across Reddit, Hacker News, X, Bluesky, and Facebook using RedReplier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and other RedReplier users monitor brand mentions, find relevant leads, manage monitored websites and keywords, and review or triage mentions from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A compromised or overbroad API token could expose or change mention and keyword data in its workspace.

Mitigation: Use a dedicated, revocable RedReplier token scoped to the intended workspace and keep it private.

Risk: Direct API deletion of a keyword removes its mentions; deleting a website stops its monitoring.

Mitigation: Require explicit user confirmation naming the keyword or website before either delete request; disable a keyword instead when preserving mentions matters.

Risk: AI-scored mentions may be mistaken for genuine leads.

Mitigation: Review the original mention and its relevance explanation before approving or rejecting it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tarasshyn/skills/redreplier)
- [RedReplier](https://redreplier.com)
- [RedReplier API reference](references/api-reference.md)
- [Mention filtering guide](references/mention-filtering.md)
- [OpenClaw plugin guide](openclaw-plugin/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with mention summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Access to workspace data requires a RedReplier API token.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
