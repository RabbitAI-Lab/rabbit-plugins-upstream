## Description:

Turns technical disclosures or an early invention idea into Chinese-language patent draft materials and review notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, R&D teams, and patent professionals use this skill to turn technical materials into a preliminary patent specification, claims outline, drawings, and review notes. For a short idea, it first proposes directions for the user to select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invention disclosures, drafts, formulas, and parameters are sent to PatentMax's remote service and may contain confidential or pre-filing material.

Mitigation: Obtain authorization before sending materials; avoid trade secrets or customer-confidential data unless your organization accepts the vendor's retention and data-residency terms.

Risk: Changing the service endpoint can send sensitive material to an unintended destination.

Mitigation: Set PATENTMAX_BASE_URL only when you intentionally trust the replacement endpoint.

Risk: An automatically generated patent draft may include inferred facts and is not ready for filing as-is.

Mitigation: Check the accompanying review notes, verify technical details, and have a patent professional finalize any application.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-writing-cn)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Materials guide](references/materials-guide.md)
- [Workflow and result guide](references/workflow.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Files, Text guidance]

**Output Format:** [Two DOCX files (patent draft and review notes); text for proposed directions and progress]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The draft includes a claims-structure preview; review notes identify inferred or missing details and invention-point comparisons.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
