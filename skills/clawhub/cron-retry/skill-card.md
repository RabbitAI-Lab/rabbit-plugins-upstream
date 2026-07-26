## Description: <br>
Auto-retry failed cron jobs on connection recovery. Use when cron jobs fail due to network errors and should be retried when connectivity is restored. Integrates with heartbeat to detect failed jobs and re-run them automatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jrbobbyhansen-pixel](https://clawhub.ai/user/jrbobbyhansen-pixel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to recover enabled cron jobs that failed because of transient network or connection errors. It provides heartbeat integration guidance and manual commands for identifying and retrying eligible jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic heartbeat retries can rerun matching enabled cron jobs without clear retry bounds or per-job approval. <br>
Mitigation: Require an explicit job allowlist, cooldown, retry cap, and recovery report before enabling automatic retry behavior. <br>
Risk: Repeated jobs can cause duplicate public posts, messages, spending, or important data changes when the underlying job is not safe to repeat. <br>
Mitigation: Do not auto-retry jobs that post publicly, send duplicate messages, spend money, or change important data unless they are idempotent and explicitly approved. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and heartbeat configuration text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces retry guidance for cron jobs and recovery status reporting language.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
