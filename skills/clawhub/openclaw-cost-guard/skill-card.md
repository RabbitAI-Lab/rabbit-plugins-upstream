## Description: <br>
Track OpenClaw/Clawdbot token and cost usage from session JSONL logs, generate daily and weekly summaries, identify expensive sessions, run budget checks, and apply token-saving guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dasweltall](https://clawhub.ai/user/dasweltall) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to monitor OpenClaw or Clawdbot spend from local session logs, summarize costs, identify high-cost sessions, and enforce budget checks for cron or alert workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cost reports and alerts may reveal usage patterns, session IDs, and local file paths. <br>
Mitigation: Keep generated reports and alert messages private, and redact sensitive identifiers before sharing. <br>
Risk: Alert integrations can expose secrets if credentials are embedded in scripts or messages. <br>
Mitigation: Store alert credentials outside scripts and avoid including secrets in generated commands or shared output. <br>
Risk: Budget checks can intentionally return a nonzero exit code when spend exceeds the configured limit. <br>
Mitigation: Test scheduled checks in warn mode before enabling exit mode in cron or alert workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dasweltall/skills/openclaw-cost-guard) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON cost reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Budget checks can exit with code 2 on breach; warn mode is available for non-failing checks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
