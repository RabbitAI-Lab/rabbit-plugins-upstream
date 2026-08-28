## Description:

凭 App Key 调用百炼®标书开放 API，帮助用户完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to process local tender and bid files through the 百炼®标书 cloud API, producing tender analysis, bid document drafts, and compliance review reports for procurement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm user consent before upload and process only the files the user explicitly selected.

Risk: The App Key grants account access and can expose the user's account if pasted into chat or shared links.

Mitigation: Have the user keep the key in a private local config file, do not echo it, and reset it on the provider site if it may have leaked.

Risk: Bid document generation consumes account points.

Mitigation: Check balance and confirm the user wants to proceed before starting generation.

Risk: Provider task results and generated documents are retained for about 7 days.

Mitigation: Disclose the retention period and direct users to manage historical results through the provider platform.

Risk: Generated bid content and compliance findings may be incomplete or require professional review before submission.

Mitigation: Require human review of generated documents, unresolved placeholders, compliance findings, and procurement-specific requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration guidance, API calls]

**Output Format:** [Text or Markdown responses with generated .docx bid documents, HTML or Word reports, and structured JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents consume account points; tender and bid files are uploaded to the provider cloud service and task results are retained by the provider for about 7 days.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
