## Description: <br>
Designs and outputs n8n workflow JSON with robust triggers, idempotency, error handling, logging, retries, and human-in-the-loop review queues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation builders use this skill to design auditable n8n workflows with clear triggers, data contracts, idempotency, retries, logging, and review queues. It can produce a workflow design spec by default, and n8n importable workflow JSON plus a runbook when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated n8n workflows may reference unintended systems, credential scopes, logging destinations, or approval steps. <br>
Mitigation: Review each generated workflow against the intended automation, credentials, logs, and approvals before installing or activating it. <br>
Risk: Workflow JSON could expose secrets if credentials are written directly into generated nodes. <br>
Mitigation: Use environment variables or named credential references only, and confirm no secrets are embedded before import. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/n8n-workflow-automation) <br>
- [Runbook template](assets/runbook-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, n8n workflow JSON when explicitly requested, and runbook Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; generated workflows are intended for review before activation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, package metadata, and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
