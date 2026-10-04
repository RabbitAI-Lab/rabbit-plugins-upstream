## Description:

协助研究者和写作者通过多角色协作、证据核查、同行评审与人工确认，完成学术论文、深度长文和行业分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

研究人员、编辑及行业分析写作者用它规划并撰写需多方证据支撑的长文，经过审阅、修订和人工把关后交付草稿及审计材料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad multi-agent authority may exceed the intended task boundaries.

Mitigation: Review the workflow before installing and enforce host-side tool restrictions for undeclared tools.

Risk: Research queries, URLs and draft content may be sent to external providers.

Mitigation: Confirm external-service consent first; use the local or redacted mode for sensitive work.

Risk: The workflow creates and updates numerous project files.

Mitigation: Approve the file scope during setup and review generated drafts and audit records before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline guide](references/pipeline-readme.md)
- [Permissions and tool boundaries](references/permissions.md)
- [External services and consent](references/_shared/真源/external-services.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown drafts, research cards, review reports and project status files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence and audit records; channel recommendations are advisory.]

## Skill Version(s):

2.15.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
