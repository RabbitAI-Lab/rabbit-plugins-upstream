## Description:

深知公文写作 helps office, secretarial, and workplace users draft, revise, review, and deliver formal Chinese documents, with optional dknowc Trusted Search for traceable policy, data, standards, and case references plus Word or red-head document output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external workplace users use this skill to turn notes, meeting records, source materials, research inputs, or rough drafts into structured formal Chinese documents. It supports common official-document and workplace-material tasks such as notices, requests, reports, letters, meeting minutes, summaries, plans, speeches, research reports, review materials, Word delivery, and optional traceable-source reports when search is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search-backed tasks may send writing context or source material to dknowc's external service.

Mitigation: Use search only when the organization permits the relevant material to be sent to the vendor service; avoid confidential, regulated, or sensitive internal content in search-backed tasks.

Risk: Search setup may require a phone number and may create or retrieve an account/API key.

Mitigation: Enable search only after the user understands the registration step and consents to using the external search service.

Risk: Search setup stores the service API key in the user's shell configuration by default.

Mitigation: Review the DKNOWC_API_KEY shell configuration block after setup and remove or rotate the key according to local credential-management policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Task router](artifact/reference/task_router.md)
- [Fact discipline](artifact/reference/fact_discipline.md)
- [Search policy](artifact/reference/search_policy.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [Document standards index](artifact/reference/standards/00_index.md)
- [dknowc dependable search endpoint](https://open.dknowc.cn/dependable/search/)
- [dknowc platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance, shell commands, generated .docx Word files, and optional HTML provenance reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write initialization state, user-approved preferences, Word documents, search intermediates, provenance reports, and a DKNOWC_API_KEY shell configuration block when search setup is used.]

## Skill Version(s):

3.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
