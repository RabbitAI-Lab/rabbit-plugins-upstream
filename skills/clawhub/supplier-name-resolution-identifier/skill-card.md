## Description:

Provides supplier-name normalization guidance for reconciliation without verifying registrations or determining canonical supplier identities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and vendor-reconciliation staff use the skill to draft a supplier-name normalization rule for review. Verify supplier identity against authoritative records before changing vendor data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation may suggest that the skill can establish canonical supplier identities, but its output only describes normalization rules.

Mitigation: Check registration identifiers and other authoritative supplier records, and have a person review ambiguous matches before changing vendor data.

## Reference(s):

- [Supplier Name Resolution Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-identifier)

## Skill Output:

**Output Type(s):** [Guidance]

**Output Format:** [JSON with a matching_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a normalization rule, not a verified supplier identity or vendor-master update.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
