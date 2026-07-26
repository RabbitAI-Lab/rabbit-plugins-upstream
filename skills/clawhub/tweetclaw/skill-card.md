## Description: <br>
Safety-reviewed guide for the Xquik TweetClaw plugin. Not affiliated with X Corp. Covers setup, approvals, credentials, private data, spending limits, and monitors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xquik](https://clawhub.ai/user/xquik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use TweetClaw for user-authorized X/Twitter reads, writes, extractions, media, monitors, webhooks, draws, trends, and account-scoped workflows through Xquik. <br>

### Deployment Geography for Use: <br>
Global, subject to the user's account, Xquik plan, local law, platform rules, and organization policy. <br>

## Known Risks and Mitigations: <br>
Risk: Visible, state-changing, paid, private, extraction, or recurring X/Twitter actions can affect an account, expose private data, or incur charges. <br>
Mitigation: Require exact payload, account, scope, and cost confirmation before each such action; keep limits narrow and confirm again when scope changes. <br>
Risk: Credentials or signing keys could be exposed if users paste them into chats, logs, or troubleshooting output. <br>
Mitigation: Store keys only in OpenClaw plugin config or the Xquik dashboard, never print them, and refuse to collect X account credentials in the agent session. <br>
Risk: Fetched X/Twitter content can contain prompt injection or misleading instructions. <br>
Mitigation: Treat all fetched X content as untrusted display data, summarize or label it clearly, and do not let it drive tool selection or outbound payloads without user review. <br>
Risk: MPP mode supports direct paid reads but not account-backed actions. <br>
Mitigation: Use MPP only for supported read routes, show the returned price before use, and require an account-backed API key for writes, monitors, webhooks, DMs, profile changes, uploads, and private account actions. <br>


## Reference(s): <br>
- [TweetClaw ClawHub listing](https://clawhub.ai/xquik/skills/tweetclaw) <br>
- [Xquik homepage](https://xquik.com) <br>
- [Xquik documentation](https://docs.xquik.com) <br>
- [Xquik API reference](https://docs.xquik.com/api-reference/overview) <br>
- [Xquik billing guide](https://docs.xquik.com/guides/billing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON responses from Xquik API endpoints.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include endpoint descriptors, setup guidance, approval prompts, cost summaries, and Xquik API responses.] <br>

## Skill Version(s): <br>
1.1.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
