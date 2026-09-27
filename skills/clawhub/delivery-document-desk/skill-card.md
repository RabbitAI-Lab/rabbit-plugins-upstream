## Description:

Determine signature requirements and compose delivery document sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and agents use this skill to determine whether a delivery requires a recipient signature and to compose the corresponding delivery-document section from supplied request data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delivery requests may contain operational details that are not needed for a signature decision.

Mitigation: Provide only the package class, service level, and signature requirement data needed for the current stage.

## Reference(s):

- [Delivery Document Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-document-desk)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Boolean value or JSON-like object with delivery document section fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied delivery request and signature requirement data; no credentials or private file access required.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
