## Description:

TinkerClaw Token Panel tracks AI token usage, budgets, provider usage APIs, optional local transcript parsing, and a localhost REST API in one dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI tool users use this skill to monitor token usage, quota status, and budget limits across Anthropic, OpenAI, Gemini, and Manus from a local dashboard and API. It is useful when users want local usage records and alerts before provider limits or monthly budgets are exceeded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Claude collector can reuse Claude Code's OAuth token when explicitly enabled.

Mitigation: Enable that collector only after reviewing the consent prompt and confirming the credential file ownership and access model are acceptable.

Risk: The local API can expose usage, quota, budget, and task data if it is reachable beyond the local machine.

Mitigation: Keep the API bound to localhost and set TOKEN_PANEL_API_TOKEN before allowing mutating endpoints.

Risk: Transcript parsing opens local session files that may contain full prompts and replies.

Mitigation: Leave TOKEN_PANEL_READ_TRANSCRIPTS disabled unless local transcript access is intended, and treat generated database and JSON usage files as sensitive.

Risk: Running the collector as a service gives it ongoing background access to configured credentials and local usage data.

Mitigation: Enable the systemd service only when continuous monitoring is needed; otherwise run collection manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/token-panel-ultimate)
- [Anthropic Usage and Cost API documentation](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
- [Google Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Manus plans documentation](https://manus.im/docs/introduction/plans)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local API responses, budget summaries, SQLite-backed usage records, and setup commands.]

## Skill Version(s):

2.4.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
