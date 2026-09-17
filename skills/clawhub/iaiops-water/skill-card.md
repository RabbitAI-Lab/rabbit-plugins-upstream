## Description:

Water-treatment edition of iaiops for waterworks, wastewater plants, and pump stations, covering Modbus-TCP/RTU, OPC-UA, HART-IP instrumentation, downtime root-cause analysis, data quality watchdogs, and OEE analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations engineers use this skill to inspect water-treatment telemetry, diagnose dataflow and downtime issues, evaluate water-quality compliance inputs, and draft site readiness or onboarding guidance for industrial water systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill claims a read-only posture while listing push, publish, and export tools that could transfer or alter operational data if available at runtime.

Mitigation: Confirm that the water profile disables push, publish, and export tools before deployment; if any remain available, require explicit approval, destination allowlists, and an isolated environment with pinned dependencies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite input values and operational context when producing diagnostics, compliance summaries, onboarding drafts, or investigation guidance.]

## Skill Version(s):

0.28.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
