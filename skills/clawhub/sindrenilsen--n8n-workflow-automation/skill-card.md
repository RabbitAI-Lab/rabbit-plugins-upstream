## Description: <br>
Designs and outputs n8n workflow JSON with robust triggers, idempotency, error handling, logging, retries, and human-in-the-loop review queues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sindrenilsen](https://clawhub.ai/user/sindrenilsen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation builders use this skill to design auditable n8n workflows with clear triggers, data contracts, idempotency, observability, retries, and human review paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated n8n workflows can affect external systems after import and activation. <br>
Mitigation: Review and test workflows before activation, keep them inactive until approved, and use least-privilege credentials. <br>
Risk: Workflow JSON could expose secrets if credentials are written directly into generated nodes. <br>
Mitigation: Reference environment variables or n8n credential names only, and do not place secrets directly in workflow JSON. <br>
Risk: Incorrect trigger, retry, or deduplication choices can duplicate records or hide failed runs. <br>
Mitigation: Confirm schedules, payload contracts, dedup keys, logging destinations, failure notifications, and review queues before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sindrenilsen/skills/n8n-workflow-automation) <br>
- [Runbook template](assets/runbook-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional n8n workflow JSON and runbook Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated workflows should remain inactive until reviewed and tested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
