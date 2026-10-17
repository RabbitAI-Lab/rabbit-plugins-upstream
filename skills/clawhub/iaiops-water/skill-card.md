## Description:

Guides water and wastewater plant monitoring across Modbus, OPC UA, and HART, with water-quality checks, data-quality monitoring, and downtime analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Plant engineers and operators use this skill to inspect water-quality instrumentation, investigate alarms and downtime, and review disinfection and water-quality checks. Confirm site-specific limits and required CT values before relying on compliance results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes a read-only profile but also lists tools that can export, push, or publish operational plant data.

Mitigation: Before use in a live plant, verify the loaded profile's actual capabilities; permit data transfers only with explicit approval, known destinations, appropriate scope, and logging.

## Reference(s):

- [iaiops-water ClawHub release](https://clawhub.ai/zw008/skills/iaiops-water)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Text and Markdown with readings, diagnostic findings, compliance comparisons, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compliance comparisons depend on supplied site-specific limits and required CT values.]

## Skill Version(s):

0.29.0 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
