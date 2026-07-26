## Description: <br>
Designs and outputs n8n workflow JSON with robust triggers, idempotency, error handling, logging, retries, and human-in-the-loop review queues for auditable automations that should not silently fail. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation builders use this skill to design n8n workflows with cron, webhook, or manual triggers; explicit data contracts; idempotency controls; retry handling; audit logging; failure notifications; and human review queues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated n8n workflow JSON can affect external systems if imported without review. <br>
Mitigation: Review nodes, destinations, credentials, logged fields, retry behavior, and review queues before importing generated JSON. <br>
Risk: Automation failures or retries can duplicate records or silently drop work if idempotency and alerts are incomplete. <br>
Mitigation: Define deduplication keys, log each run, add failure notifications, and route unresolved failures to a human review queue. <br>
Risk: Secrets could be exposed if embedded directly in workflow JSON. <br>
Mitigation: Keep secrets out of generated JSON and reference environment variables or n8n credential names instead. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kowl64/skills/n8n-workflow-automation) <br>
- [Runbook template](artifact/assets/runbook-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with optional importable n8n workflow JSON and runbook Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; workflow JSON is produced only when explicitly requested, with secrets referenced by environment variables or credential names.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
