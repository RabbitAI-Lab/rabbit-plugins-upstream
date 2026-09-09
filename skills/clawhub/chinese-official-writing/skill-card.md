## Description:

帮助机关、企事业单位、学校和新闻机构起草、改写、压缩和复核中文公文、事务性材料、新闻稿件及相关正式文本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external writers, and administrative teams use this skill to draft, revise, compress, and review Chinese official documents, institutional rules, reports, notices, speeches, news copy, feasibility-review materials, and AI-compute service documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parsing hostile or unusually large DOCX inputs may cause local denial of service.

Mitigation: Run the optional prose linter only on trusted, reasonably sized documents in a host with time and memory limits.

Risk: Optional Hook or Pro resources are outside the packaged skill and may have a different behavior or security posture.

Mitigation: Review any external Hook or Pro resources separately before enabling them outside the packaged skill.

## Reference(s):

- [README](artifact/README.md)
- [Skill Instructions](artifact/SKILL.md)
- [Writing Workflow](artifact/references/workflow.md)
- [Genre Routing](artifact/references/genre-routing.md)
- [Information Selection](artifact/references/information-selection.md)
- [Handling Elements](artifact/references/handling-elements.md)
- [Final Review Layers](artifact/references/final-review-layers.md)
- [GB/T 9704 Format Reference](artifact/references/format-gbt9704.md)
- [AI Compute Documents](artifact/references/ai-compute-docs.md)
- [Optional Hook Usage](https://github.com/gongyu0918-debug/chinese-official-writing-skill/blob/main/chinese-official-writing/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Plain text or Markdown, with optional shell commands for local prose linting when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return full drafts, revised bodies, concise review notes, formatting guidance, or optional linter commands; it should not invent unsupported official facts.]

## Skill Version(s):

1.6.31 (source: evidence release, target metadata, and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
