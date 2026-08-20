## Description:

深知公文写作 helps office, administrative, secretarial, and enterprise users draft, revise, review, and deliver formal Chinese official documents, workplace reports, speeches, summaries, plans, and traceable source reports when search is used.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Office, administrative, secretarial, and enterprise users use this skill to turn notes, meeting records, research material, or draft text into structured formal Chinese documents and Word deliverables. When policy, data, standards, or case support is needed, it can use DKnowC services and create a separate source-traceability report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search activation may require a phone number and external DKnowC service calls for writing or search requests.

Mitigation: Use the skill only where this external processing is approved, and avoid sending confidential official drafts unless the organization has authorized that workflow.

Risk: The skill may persist a DKNOWC_API_KEY block in the user's shell profile.

Mitigation: Prefer a platform secret manager or a one-session environment variable when available, and review shell-profile changes after search setup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer)
- [DKnownAI Publisher Profile](https://clawhub.ai/user/dknownai)
- [Skill README](artifact/README.md)
- [Output Guide](artifact/reference/output_guide.md)
- [Search Policy](artifact/reference/search_policy.md)
- [Review Checklist](artifact/reference/review_checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions and generated Word documents, with optional HTML source-traceability reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local reference files, user-confirmed local memory, DKnowC services for search-backed material, and an API key when search is needed.]

## Skill Version(s):

3.4.2 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
