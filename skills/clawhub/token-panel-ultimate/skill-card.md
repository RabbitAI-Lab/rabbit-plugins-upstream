## Description:

Tracks AI token usage across Anthropic, Gemini, OpenAI, and Manus with budget alerts and a localhost REST API dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to monitor multi-provider token usage, budget status, and rate-limit context from local scripts and a localhost dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Claude credential borrowing can weaken credential separation when TOKEN_PANEL_USE_CLAUDE_CREDENTIALS is enabled.

Mitigation: Leave TOKEN_PANEL_USE_CLAUDE_CREDENTIALS disabled and prefer dedicated provider keys stored through secretstore.py.

Risk: The localhost API reports usage and quota data and should not be exposed beyond the local machine.

Mitigation: Bind the API to localhost, do not publish the port, and require TOKEN_PANEL_API_TOKEN for mutating endpoints.

Risk: The Manus/task output database may contain task or prompt snippets.

Mitigation: Treat the local SQLite database as sensitive and avoid storing sensitive task descriptions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/token-panel-ultimate)
- [Budget README](BUDGET_README.md)
- [Anthropic Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Manus plans documentation](https://manus.im/docs/introduction/plans)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local credential setup, localhost API use, and budget database operation.]

## Skill Version(s):

2.5.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
