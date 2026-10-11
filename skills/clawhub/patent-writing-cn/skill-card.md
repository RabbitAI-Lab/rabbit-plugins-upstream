## Description:

Generates Chinese-language patent first drafts and review notes from technical disclosures, R&D materials, or a selected invention idea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, engineers, and patent professionals use the skill to turn technical materials into a Chinese patent draft, with separate notes flagging assumptions and missing details for human review. For a preliminary idea, it can propose directions before drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invention disclosures, ideas, and technical materials are sent to an external PatentMax service.

Mitigation: Submit only authorized materials after reviewing the provider's confidentiality and retention terms; avoid confidential, client-owned, export-controlled, or pre-filing IP without authorization.

Risk: Drafting is a paid service and duplicate requests may incur additional charges.

Mitigation: Get user confirmation before submission, check task status rather than resubmitting while work is in progress, and review the available balance.

Risk: Drafts may contain inferred details and patent comparisons are not formal novelty opinions or grant guarantees.

Mitigation: Review the separate notes with the inventor and have a patent professional verify claims, technical facts, and filing readiness.

Risk: An unexpected PATENTMAX_BASE_URL value can route submitted materials to a different destination.

Mitigation: Check the configured service URL before submitting invention materials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-writing-cn)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Materials preparation guide](references/materials-guide.md)
- [Drafting workflow](references/workflow.md)
- [Troubleshooting FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown guidance and downloadable Word (.docx) documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a patent draft and separate review notes; idea directions and task status are summarized in text.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
