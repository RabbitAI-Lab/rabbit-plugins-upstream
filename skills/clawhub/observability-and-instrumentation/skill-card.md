## Description: <br>
Add observability and instrumentation to applications �� metrics, logs, traces, and dashboards <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add production observability to applications through structured logs, metrics, distributed traces, dashboards, and actionable alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Telemetry changes may increase observability platform cost or create high-cardinality metric labels. <br>
Mitigation: Review generated instrumentation for bounded label sets, sampling choices, and expected series volume before deployment. <br>
Risk: Logs or traces may accidentally expose PII, secrets, tokens, or complete request bodies. <br>
Mitigation: Require field allowlists, redaction checks, and review of actual emitted telemetry before production rollout. <br>
Risk: Alert proposals may create noisy or non-actionable notifications. <br>
Mitigation: Validate alerts against user-facing symptoms, sustained thresholds, ownership, routing, and runbook links before enabling paging. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code examples, checklists, and implementation recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose instrumentation, logging, metrics, tracing, dashboard, and alerting changes for human review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
