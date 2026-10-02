## Description:

面向学术论文、深度文章和行业分析的多角色写作流程，涵盖资料研究、起草、审计和同行评审。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and researchers use this skill to plan, research, draft and review evidence-based long-form articles or academic manuscripts, with user approval before research or file creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates many files and maintains local status and audit records.

Mitigation: Confirm the Phase 0 scope and file choices before starting; review generated records before sharing.

Risk: Web research can send queries and URLs to external services.

Mitigation: Decline external services for sensitive material and approve research choices during Phase 0.

Risk: Status records can contain telemetry or session-related details.

Mitigation: Redact telemetry and session-related fields before sharing status.md.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](artifact/QUICKSTART.md)
- [Pipeline overview](artifact/references/_shared/真源/pipeline-overview.md)
- [External services and consent](artifact/references/_shared/真源/external-services.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown articles, research notes, review reports and project status records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates multiple project files after the user confirms the workflow.]

## Skill Version(s):

2.15.8 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
