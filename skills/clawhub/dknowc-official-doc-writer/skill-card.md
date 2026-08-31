## Description:

深知公文写作 is a formal-document writing assistant for office, administrative, secretary, materials, enterprise, and public-sector users that helps draft, revise, polish, review, format, and deliver official documents, reports, summaries, speeches, meeting minutes, plans, research materials, Word documents, and optional traceable source reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external workplace users use this skill to turn notes, meeting records, research material, or rough drafts into structured formal Chinese documents. It supports drafting, revision, review, Word delivery, optional red-head formatting, and source-trace reporting when search-backed evidence is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search onboarding asks the user for a phone number and SMS code and provisions access with a provider-managed API key.

Mitigation: Install only when that account flow is acceptable for the deployment; prefer platform-managed secrets or manual token setup where policy requires it.

Risk: The skill may send search and outline queries to dknowc services.

Mitigation: Do not send confidential draft content or sensitive organizational material as search queries unless the organization explicitly allows it.

Risk: The registration helper can persist an API key in ~/.zshrc.

Mitigation: Use a platform secret store or manually managed token when possible, and remove or rotate the local key if the skill is no longer used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Search policy](artifact/reference/search_policy.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [Revision workflow](artifact/reference/revision_workflow.md)
- [Official document standards index](artifact/reference/standards/00_index.md)
- [Dknowc trusted search endpoint](https://open.dknowc.cn/dependable/search/)
- [Dknowc MCP endpoint](https://mcp.dknowc.cn/s6/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose, command snippets, JSON helper-script status, DOCX files, and HTML source-trace reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search-backed work may require DKNOWC_API_KEY; the artifact can generate Word documents and HTML trace reports and can store user-authorized local writing preferences or materials.]

## Skill Version(s):

3.4.5 (source: frontmatter and server release evidence, released 2026-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
