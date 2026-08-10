## Description:

深知公文写作 helps office, administrative, secretarial, and enterprise users draft, revise, review, and deliver formal Chinese workplace and official documents, with optional trusted search for policy, data, standards, and case references plus Word and red-head document output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external business users use this skill to produce formal Chinese documents such as notices, requests, reports, letters, meeting minutes, summaries, plans, speeches, research reports, and management materials. For tasks needing policy, data, standards, or examples, it can retrieve traceable supporting material and generate a separate source report before delivering editable Word output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and outline workflows can send prompts, draft context, and requested reference topics to dknowc remote services.

Mitigation: Use search only for approved material, avoid confidential or restricted content unless the organization approves the data flow, and rely on non-search writing modes for sensitive drafts.

Risk: Search onboarding may require phone and SMS verification handled by the agent.

Mitigation: Use this workflow only when the user intentionally enables search access, and prefer administrator-managed setup or a platform secret store in managed environments.

Risk: The default setup can store a long-lived DKNOWC_API_KEY in ~/.zshrc.

Mitigation: Review the stored credential location, rotate or remove the key when no longer needed, and use a secret manager or manual provider configuration where policy requires it.

Risk: Generated official documents may contain incorrect, incomplete, or unsuitable policy references or formal wording.

Mitigation: Have a qualified reviewer check facts, source reports, formatting, authority, and final wording before external or official use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer)
- [README](artifact/README.md)
- [Search policy](artifact/reference/search_policy.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [Task router](artifact/reference/task_router.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, Chinese formal-document text, editable .docx files, optional red-head .docx files, HTML traceability reports, and JSON search intermediates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search-dependent workflows may require a DKNOWC_API_KEY, user confirmation before search, and local Python and Node.js dependencies.]

## Skill Version(s):

3.3.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
