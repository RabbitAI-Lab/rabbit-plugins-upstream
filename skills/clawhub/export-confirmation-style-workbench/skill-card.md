## Description:

Creates a local delivery acknowledgement receipt and returns a confirmation result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People handling routine deliveries use this skill to create a local acknowledgement after completion and receive a confirmation result for the current operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local receipt could be mistaken for proof of real-world delivery.

Mitigation: Treat the receipt as a local acknowledgement only; verify actual delivery separately.

Risk: Running the skill writes receipt files to the selected output directory.

Mitigation: Provide only intended request data and choose a dedicated writable output directory.

## Reference(s):

- [Delivery Receipt Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON confirmation result and local receipt file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports operation ID, confirmation status, and whether a receipt was created.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
