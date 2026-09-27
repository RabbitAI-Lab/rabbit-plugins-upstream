## Description:

Helps agents monitor and triage keyword mentions across Reddit, Hacker News, X, and Bluesky using RedReplier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Brand teams and developers use this skill to monitor social discussions about their products, review AI-scored leads, manage monitored sites and keywords, and configure mention alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token grants access to monitored sites, keywords, mention content, and triage state.

Mitigation: Use a dedicated revocable token and send it only to the documented RedReplier service.

Risk: Manual API keyword activation or re-enabling can charge the account.

Mitigation: Preview any charge and obtain explicit approval before activating keywords.

Risk: Manual deletion can stop website monitoring or remove keyword history.

Mitigation: Confirm the named target with the user before deletion; disable a keyword instead when appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tarasshyn/skills/redreplier)
- [RedReplier](https://redreplier.com)
- [RedReplier API reference](references/api-reference.md)
- [Mention filtering guide](references/mention-filtering.md)
- [OpenClaw plugin guide](openclaw-plugin/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize scored mentions and suggest actions for user approval.]

## Skill Version(s):

1.0.5 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
