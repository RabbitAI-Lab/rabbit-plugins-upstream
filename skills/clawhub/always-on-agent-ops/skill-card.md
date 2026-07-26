## Description: <br>
Keeps an OpenClaw agent running continuously by guiding loopback gateway setup, cron health checks, OAuth expiry checks, queue preflights, event dispatch, and retention cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to keep an OpenClaw agent alive on a dedicated host, diagnose quiet failures, and configure outbound polling, cron jobs, notifications, and cleanup routines for unattended operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unattended cron jobs and agent turns can run with more authority than intended if the host, queue tokens, or tool profiles are not scoped. <br>
Mitigation: Install only on a dedicated, physically secured host; use scoped queue tokens; keep secrets.env chmod 600 and out of git; and verify every cron job ID and tool profile before enabling unattended runs. <br>
Risk: Queue polling and notifications can send data to external systems chosen by the operator. <br>
Mitigation: Confirm that queue and notification destinations are systems the operator is authorized to use, and keep secrets, PII, and payload dumps out of status messages. <br>
Risk: Expired OAuth profiles, incorrect cron IDs, or phase-locked fallback schedules can make the agent appear healthy while work is missed or duplicated. <br>
Mitigation: Prefer non-expiring API keys when appropriate, alert on OAuth warn or missing states, verify installed cron IDs with OpenClaw, and use explicit cron minutes for heavy fallback jobs. <br>
Risk: Retention cleanup deletes local log files. <br>
Mitigation: Limit deletion to regular .log files under a verified OpenClaw home, configure the retention window deliberately, and use the dry-run mode before applying a new cleanup policy. <br>


## Reference(s): <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/always-on-agent-ops) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with bash, JSON, JSON5, and status-line examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational checklists, cron conventions, and shell helper behavior for always-on OpenClaw hosts.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
