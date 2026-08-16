## Description:

标书智能制作工具，凭 App Key 调用开放 API 完成评分点应答与排版：解读招标文件评分标准与废标红线、按目标页数生成成品投标文件(.docx)、技术标商务标应答撰写、合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender documents, generate editable bid documents, and review bid files for compliance risks after providing local tender or bid files. The workflow uses the 百炼®标书 cloud API and requires user consent before uploading commercially sensitive documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user awareness and consent before upload, and process only files the user explicitly selected or identified by local path.

Risk: The App Key is an account credential stored in the skill directory and can expose account access if pasted into chat or shared through links.

Mitigation: Have the user create config.json locally, keep it permission-restricted, and never request, display, or forward App Key values or bind_key links.

Risk: Changing ZCM_BASE or a stored base URL can send credentials and uploaded documents to an alternate endpoint.

Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user intentionally trusts the alternate API endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-radar)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage reference](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Agent guidance plus generated JSON results, HTML or Word reports, and editable .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads user-selected local tender or bid files; writes outputs under biaoshu-bailian-files/ or a user-selected output path.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
