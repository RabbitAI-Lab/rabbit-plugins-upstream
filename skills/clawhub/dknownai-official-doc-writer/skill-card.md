## Description:

深知公文写作 helps office, administrative, secretarial, and business users draft, revise, review, and package formal Chinese official documents and workplace materials, with optional traceable search support for policy, data, standards, and case references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users in office, administrative, secretarial, and business-document roles use this skill to turn notes, meeting records, drafts, and research materials into formal Chinese documents such as notices, requests, reports, letters, meeting minutes, plans, summaries, speeches, and research reports. When a task needs current policy, data, standards, or cases, it can retrieve supporting material and produce a separate traceability report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search activation provisions an account and stores a service API key in ~/.zshrc.

Mitigation: Review the installation before use, use a dedicated workspace or account, and remove or revoke the key when it is no longer needed.

Risk: Writing and search queries may be processed by the external search service when search is enabled.

Mitigation: Use search only when needed for policy, data, standards, or case support, and avoid submitting content that is not approved for that service.

Risk: Generated official documents can contain unsupported facts or formatting issues if source material is incomplete.

Mitigation: Review generated documents with the bundled fact discipline, review checklist, and traceability report before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer)
- [DKnownAI publisher profile](https://clawhub.ai/user/dknownai)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Task router](artifact/reference/task_router.md)
- [Search policy](artifact/reference/search_policy.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [Fact discipline](artifact/reference/fact_discipline.md)
- [Anti-AI-pattern guidance](artifact/reference/anti_ai_patterns.md)
- [Document standards index](artifact/reference/standards/00_index.md)
- [DKnowC search endpoint](https://open.dknowc.cn/dependable/search/)
- [DKnowC management platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance plus generated .docx Word documents, optional red-head .docx files, HTML traceability reports, and JSON search artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python dependencies for document generation; search tasks may require phone-based activation and a service API key.]

## Skill Version(s):

3.4.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
