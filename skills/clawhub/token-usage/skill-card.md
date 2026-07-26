## Description: <br>
Track, aggregate, and report OpenClaw token usage and costs across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to review OpenClaw token usage, estimate costs, compare model or session activity, and monitor budget trends from local session logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local OpenClaw session logs to compute usage and cost reports. <br>
Mitigation: Install and run it only in environments where reading local session logs is acceptable. <br>
Risk: Session archive commands can compress or move local session files. <br>
Mitigation: Review archive commands before execution and keep backups or retention requirements in mind. <br>
Risk: The pricing updater and SQLite ingestion helper can update local pricing files or usage.db. <br>
Mitigation: Run those maintenance helpers only when local pricing data or the usage database should be updated. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/token-usage) <br>
- [Skill Homepage](https://github.com/space-cadet/openclaw-tools/tree/main/skills/token-usage) <br>
- [OpenRouter Models API](https://openrouter.ai/api/v1/models) <br>
- [Kimi Pricing Documentation](https://platform.kimi.com/docs/pricing/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, terminal summaries, and optional JSON exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cost values are estimates based on local pricing data and may differ from actual billing.] <br>

## Skill Version(s): <br>
2.2.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
