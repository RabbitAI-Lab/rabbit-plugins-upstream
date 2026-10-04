## Description:

Determines whether a delivery requires a signature and composes a delivery signature section.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff and agents use this skill to decide whether a handoff requires a recipient signature and prepare the corresponding delivery-document section.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The compose step writes a local delivery-document record that could be mistaken for a finalized business record.

Mitigation: Use a dedicated output directory and review generated files before treating them as business records.

## Reference(s):

- [Delivery Document Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-document-desk)
- [Package usage and operation details](artifact/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON decision and delivery-document section]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The compose step writes a local JSON artifact in the selected output directory.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
