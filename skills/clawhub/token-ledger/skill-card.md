## Description: <br>
Token Ledger records OpenClaw model-call token usage and costs into a local SQLite ledger, manages a watcher, and supports SQL-based usage, cost, and reconciliation reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw token consumption, costs, and source breakdowns across interactive sessions, cron jobs, and local Spark usage. It is useful for daily finance reports, historical reconciliation, and keeping provider pricing provenance with ledger entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local privacy exposure from reading OpenClaw session, cron, and Spark usage logs and storing session, chat, and thread identifiers in a persistent SQLite ledger. <br>
Mitigation: Install only where that local audit trail is acceptable, restrict access to ~/.openclaw/ledger.db and related checkpoints, and apply the user's retention policy to ledger data. <br>
Risk: Continuous background monitoring when the macOS LaunchAgent watcher is installed. <br>
Mitigation: Use one-shot or backfill commands when continuous monitoring is not needed, and unload the LaunchAgent to stop the watcher. <br>
Risk: Spark sync depends on LOCAL_API_HUB_URL and can read from a local API endpoint or local Spark token logs. <br>
Mitigation: Keep LOCAL_API_HUB_URL pointed at a trusted loopback endpoint and avoid configuring it to untrusted network services. <br>
Risk: Ledger totals may differ from provider billing because provider-side retries, timeouts, streaming interruptions, or pricing changes can affect final charges. <br>
Mitigation: Use provider billing exports for reconciliation and keep versioned price records with effective timestamps and source URLs. <br>


## Reference(s): <br>
- [Token Ledger ClawHub homepage](https://clawhub.ai/jonathanjing/token-ledger) <br>
- [Token Ledger ClawHub skill page](https://clawhub.ai/jonathanjing/skills/token-ledger) <br>
- [Anthropic Claude pricing documentation](https://platform.claude.com/docs/en/about-claude/pricing) <br>
- [OpenAI model documentation](https://developers.openai.com/api/docs/models) <br>
- [Google Gemini API pricing documentation](https://ai.google.dev/gemini-api/docs/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, SQL] <br>
**Output Format:** [Markdown guidance with shell commands, SQL queries, generated configuration, SQLite ledger entries, and tabular text reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and queries a local SQLite ledger at ~/.openclaw/ledger.db and can run as either one-shot commands or a local watcher.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and openclaw frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
