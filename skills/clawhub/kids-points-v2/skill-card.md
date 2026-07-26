## Description: <br>
Kids Points V2 helps families track child reward points through Feishu chat messages, using SQLite storage, LLM-based intent parsing, and a CLI-backed runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cowboy231](https://clawhub.ai/user/cowboy231) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and family automation builders use this skill to record, query, and review child reward-point transactions from Feishu group or direct messages. Developers can also call the CLI directly or connect the optional dashboard extension to a local SQLite ledger. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes Feishu message text, uses an LLM API key, and writes family point records to a local SQLite ledger. <br>
Mitigation: Use a dedicated skill-scoped API key through an explicit environment variable, review what Feishu messages are routed to the bot, and keep the SQLite ledger in a trusted local runtime directory. <br>
Risk: A user-controlled KIDS_POINTS_RUNTIME_DIR can redirect execution to another runtime path. <br>
Mitigation: Set KIDS_POINTS_RUNTIME_DIR only to trusted code owned by the operator, or leave it unset to use the bundled runtime. <br>
Risk: The optional dashboard exposes local service endpoints intended for localhost or a trusted LAN. <br>
Mitigation: Bind the dashboard to local or trusted network interfaces and add access control before exposing it beyond the operator's LAN. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cowboy231/skills/kids-points-v2) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Dashboard Extension README](artifact/extensions/dashboard/README.md) <br>
- [Dashboard Architecture Notes](artifact/extensions/dashboard/docs/architecture.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text responses with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write to a local SQLite ledger through the runtime CLI and may return balance, daily summary, history, or transaction result text.] <br>

## Skill Version(s): <br>
2.0.7 (source: frontmatter, release evidence, changelog released 2026-07-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
