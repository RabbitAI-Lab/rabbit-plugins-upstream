## Description:

dknowc official doc writer helps office, secretarial, administrative and enterprise users draft, revise, review and deliver structured Chinese official documents, workplace materials, Word documents and traceable source reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external business users use this skill to turn notes, meeting records, research material or rough drafts into formal Chinese government-style and workplace documents. It supports drafting, rewriting, polishing, structure adjustment, content review, Word delivery, red-head document generation when requested, and traceable source reports when search-backed evidence is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send writing and search prompts to a third-party dknowc service during account setup, search, outline retrieval, or traceability workflows.

Mitigation: Use only with material your organization permits to be shared with that provider, and avoid sensitive internal drafts unless the data flow has been approved.

Risk: The initialization and registration flow can persist DKNOWC_API_KEY in ~/.zshrc.

Mitigation: Prefer pre-configuring DKNOWC_API_KEY through a scoped secret store or controlled environment variable, and review shell profile changes after setup.

Risk: The security verdict is suspicious because initialization and third-party account setup are required even for tasks that may not need search.

Mitigation: Review the skill before installing, run it in a controlled workspace, and confirm setup behavior before using it for production documents.

Risk: Generated official documents, search-backed claims, and formatting may affect business or administrative decisions if used without review.

Mitigation: Have a responsible human review generated documents, placeholders, cited support, Word formatting, and traceability reports before external delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer)
- [README](artifact/README.md)
- [Task router](artifact/reference/task_router.md)
- [Search policy](artifact/reference/search_policy.md)
- [Material usage guidance](artifact/reference/material_usage_guidance.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [dknowc Trusted Search endpoint](https://open.dknowc.cn/dependable/search/)
- [dknowc MaaS platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, generated .docx files, optional red-head .docx files, JSON search artifacts, and HTML traceability reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, python-docx, requests, Node.js for account registration, and a DKNOWC_API_KEY environment variable before normal use.]

## Skill Version(s):

3.3.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
