## Description:

Helps pharmaceutical plant teams inspect cleanroom conditions, purified-water systems, and equipment data across BACnet, Modbus, HART-IP, and OPC-UA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical operations, automation, and validation teams use this skill to review cleanroom pressure and particle measurements, assess purified-water readings against site-approved limits, and investigate equipment and process data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The read-only description does not cover a high-impact BACnet property write path.

Mitigation: Disable or tightly gate writes with site-level authorization and change-control approval; do not authorize cleanroom or life-safety changes without explicit review.

Risk: Export, historian push, stream publish, and evidence-bundle functions can move sensitive plant data.

Mitigation: Disable these paths unless explicitly approved; restrict destinations and file access under site policy.

Risk: Incorrect site-provided quality limits or room relationships could make checks misleading.

Mitigation: Use approved site limits and verified room relationships, and have qualified personnel review results before making GMP decisions.

## Reference(s):

- [ClawHub iaiops-pharma release](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Site-approved limits and room relationships must be provided for applicable checks.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
