## Description:

深知公文写作 helps office, administrative, secretarial, and enterprise users draft, revise, review, and deliver formal Chinese workplace documents with optional DKnowC Trusted Search sourcing, Word output, red-head formatting, and HTML provenance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Office staff, administrative teams, secretarial roles, and enterprise or public-sector users use this skill to turn notes, meeting records, source materials, and drafts into formal Chinese documents. It also supports review of existing Word documents, .docx delivery, optional red-head formatting, and separate source-trace HTML when search-backed materials are used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses DKnowC remote MaaS and search services, including phone-number and SMS-code account setup.

Mitigation: Install and run it only in environments where this remote-service dependency and account setup flow are acceptable for the documents being handled.

Risk: The registration flow can persistently store DKNOWC_API_KEY in ~/.zshrc.

Mitigation: Prefer a platform secret store or session-only environment variable for sensitive-document workflows or shared machines, and remove or rotate the shell-profile key when it is no longer appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [Publisher Profile](https://clawhub.ai/user/dylanzhangzx)
- [DKnowC Open Service](https://open.dknowc.cn/)
- [DKnowC MaaS Platform](https://platform.dknowc.cn/)
- [Task Router](reference/task_router.md)
- [Search Policy](reference/search_policy.md)
- [Search Guide](reference/search_guide.md)
- [Material Usage Guidance](reference/material_usage_guidance.md)
- [Output Guide](reference/output_guide.md)
- [Review Checklist](reference/review_checklist.md)
- [Official Document Standards Index](reference/standards/00_索引.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or text guidance, shell commands, JSON intermediates, .docx Word documents, and HTML provenance reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal delivery is a Word .docx for formal documents; searched materials can produce a separate HTML provenance report. The artifact states that automatic PDF generation is not supported.]

## Skill Version(s):

3.3.0 (source: evidence.json release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
