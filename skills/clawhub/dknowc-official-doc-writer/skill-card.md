## Description:

dknowc official doc writer helps office, administrative, secretarial, and enterprise users draft, revise, review, and deliver structured formal documents, with optional trusted search support for traceable policy, data, standards, and case references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, office staff, secretarial teams, and business users use this skill to turn notes, meeting records, source materials, or rough drafts into formal documents such as notices, reports, letters, meeting minutes, summaries, plans, speeches, and research reports. When a task needs policy support, data, standards, or reference cases, the skill can retrieve traceable materials and generate a separate verification report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search onboarding may create or retrieve an API key and store it persistently in ~/.zshrc.

Mitigation: Install only after reviewing the onboarding flow, and proceed with phone verification and persistent key storage only with clear user consent.

Risk: Generated documents and verification reports may be delivered or copied to local output locations.

Mitigation: Confirm the intended delivery directory before handling sensitive documents.

Risk: The skill can maintain a local knowledge base and writing preferences for reuse.

Mitigation: Save sensitive materials to the local knowledge base only when the user intentionally wants future reuse.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [README](artifact/README.md)
- [Search Policy](artifact/reference/search_policy.md)
- [Output Guide](artifact/reference/output_guide.md)
- [Review Checklist](artifact/reference/review_checklist.md)
- [Document Standards Index](artifact/reference/standards/00_index.md)
- [dknowc Open Service](https://open.dknowc.cn/)
- [dknowc Trusted Search Endpoint](https://open.dknowc.cn/dependable/search/)
- [dknowc Platform](https://platform.dknowc.cn/)
- [dknowc MCP Server](https://mcp.dknowc.cn/s6/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown or formal-document text, generated .docx files, optional red-head .docx files, and optional HTML verification reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search-dependent tasks may produce JSON/search intermediates and source verification artifacts; PDF generation is not supported by the artifact.]

## Skill Version(s):

3.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
