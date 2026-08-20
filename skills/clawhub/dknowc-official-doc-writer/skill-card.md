## Description:

深知公文写作 helps office, secretarial, administrative, and enterprise users draft, revise, review, and deliver formal workplace documents, with optional dknowc Trusted Search support for traceable policy, data, standards, and case references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, office staff, secretarial teams, administrative roles, and enterprise users use this skill to produce official documents, letters, reports, meeting minutes, speeches, plans, summaries, research materials, and related business documents. When a task needs current policy, data, standards, or examples, the skill can use dknowc Trusted Search to prepare source-backed material and a separate traceability report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The search registration flow can require a user phone number and may create or retrieve dknowc search credentials.

Mitigation: Use only after user approval, prefer a pre-provisioned key or managed secret store, and avoid exposing the full key in conversation or public files.

Risk: The skill can write a search API key to ~/.zshrc for later sessions.

Mitigation: Review the shell-profile change before deployment and consider replacing local shell-profile persistence with platform secret storage.

Risk: External outline and search calls may receive document prompts or source material.

Mitigation: Do not send confidential, regulated, or sensitive draft content to the external services unless the user has approved that data flow.

Risk: Formal documents, policy references, data, and official wording can be incorrect or stale if generated without adequate review.

Mitigation: Require human review of final documents and source traceability reports before submission, publication, or operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [Artifact README](artifact/README.md)
- [Task router reference](artifact/reference/task_router.md)
- [Search policy reference](artifact/reference/search_policy.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [dknowc Trusted Search endpoint](https://open.dknowc.cn/dependable/search/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown-formatted document content, Word .docx files, optional red-head Word documents, and optional HTML traceability reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Python, python-docx, requests, Node.js for registration flow, and DKNOWC_API_KEY only when dknowc Trusted Search is needed.]

## Skill Version(s):

3.4.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
