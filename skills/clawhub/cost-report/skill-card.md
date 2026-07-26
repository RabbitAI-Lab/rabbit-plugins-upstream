## Description: <br>
Track OpenClaw usage costs and provide detailed reports by date and model, with text, JSON, and Discord-oriented report formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentqiu](https://clawhub.ai/user/vincentqiu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to inspect OpenClaw session logs and summarize model spend by date and model. It supports ad hoc local reports and scheduled reporting workflows for cost visibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Discord-oriented reports and --show-errors can expose raw session-log error details that may contain private prompts, identifiers, or provider messages. <br>
Mitigation: Avoid report_discord.sh and --show-errors unless the destination is trusted and the output has been reviewed or sanitized. <br>
Risk: The Node CLI forwards command-line arguments through a shell, which is unsafe for untrusted input. <br>
Mitigation: Prefer running scripts/cost_report.sh directly with simple trusted flags, and do not pass user-controlled arguments to the Node CLI. <br>
Risk: The skill reads local OpenClaw session logs, which can contain sensitive operational metadata. <br>
Mitigation: Run it only in environments where the operator is allowed to inspect those logs, and limit automated delivery to approved channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentqiu/skills/cost-report) <br>
- [OpenClaw JSONL log format](artifact/references/JSONL_FORMAT.md) <br>
- [Cron report examples](artifact/config/cron-examples.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text, Discord-formatted text, JSON reports, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and read access to local OpenClaw session JSONL logs; reports may include model totals, token counts, calls, comparison percentages, and optional error details.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
