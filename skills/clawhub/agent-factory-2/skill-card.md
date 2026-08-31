## Description:

Autonomous sub-agent factory for OpenClaw: recurring workload detection, sandboxed synthesis, 4D benchmark evaluation vs generalist baseline, dynamic vector routing, and lifecycle drift monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent-platform operators use this skill to identify recurring OpenClaw workloads, synthesize specialized disposable sub-agents, benchmark them against a generalist baseline, route matching tasks, and monitor lifecycle drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact automation can create, benchmark, promote, and route to specialized sub-agents before controls are independently enforced.

Mitigation: Use the skill only in a contained development workspace until real sandboxing and an independently enforced evaluation gate are added before promotion.

Risk: Dashboard and automation endpoints can expose control actions, prompts, or telemetry if run without access controls.

Mitigation: Add dashboard authentication and authorization, and apply telemetry redaction and retention controls before using sensitive prompts or production workflows.

Risk: Generated bundles and manifests can be trusted too broadly if archive validation and signing-key management are weak.

Mitigation: Validate archives before import, manage signing keys outside the repository and environment defaults, and verify signatures before routing to generated sub-agents.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/samajesteduroyaume/Agent-Factory)
- [ClawHub release page](https://clawhub.ai/samajesteduroyaume/skills/agent-factory-2)
- [OpenClaw](https://openclaw.ai)
- [Sub-agent manifest schema](skills/agent-factory/references/manifest_schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with CLI commands and generated JSON manifests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local telemetry, sub-agent manifests, evaluation datasets, signatures, and exported bundles inside the workspace.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
