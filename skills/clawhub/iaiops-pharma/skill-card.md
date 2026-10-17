## Description:

Helps pharmaceutical plant teams inspect cleanroom conditions, pharmaceutical water systems, and industrial equipment across BACnet, Modbus, HART, and OPC-UA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical manufacturing engineers and quality teams use this skill to review cleanroom pressure cascades, particle counts, purified water and water-for-injection measurements, and equipment evidence against site-approved requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only wording, the documented BACnet property-write path could change industrial control settings.

Mitigation: Disable the write-capable path for read-only use. In live or regulated plants, require site-specific authorization, management of change, named approval, and dry-run review before any write.

Risk: Incorrect or missing site limits and room-door relationships can make cleanroom or water assessments misleading.

Mitigation: Provide approved quality limits and verified room topology; review ungraded or unevaluated results rather than treating them as compliant.

## Reference(s):

- [iaiops-pharma ClawHub release](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Text and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing limits or readings without treating them as passes; cites measurements and supplied thresholds where available.]

## Skill Version(s):

0.29.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
