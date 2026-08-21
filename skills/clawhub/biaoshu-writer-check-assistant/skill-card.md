## Description:

基于百炼®标书开放服务，帮助用户解读招标文件、生成投标文件并审查投标文件的废标与合规风险，上传前需确认用户知悉文件会发送至百炼®标书云端处理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and proposal staff use this skill to analyze Chinese tender documents, produce editable bid documents, and run pre-submission compliance checks against tender requirements.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain sensitive commercial, pricing, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm user awareness and authorization before upload, and avoid processing files that cannot be shared with the third-party service.

Risk: The local App Key is a full account credential and could be exposed through chat logs, screenshots, or key-bearing billing links.

Mitigation: Have the user store the key only in the local config file, keep file permissions restrictive, never paste the key into chat, and share only ordinary service URLs without credential parameters.

Risk: If the service base URL is overridden, documents and the App Key could be sent away from the documented official endpoint.

Mitigation: Before use, verify ZCM_BASE and any stored base setting are unset or point only to https://biaoshu.zhiliaobiaoxun.com/api/open/v1.

Risk: Generated bid content and compliance findings may be incomplete or may miss project-specific legal, commercial, or formatting requirements.

Mitigation: Treat generated documents and reports as drafting and review aids; require qualified human review before bid submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-check-assistant)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书 open API contract](references/api.md)
- [Execution and usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown/text responses plus generated HTML, Word, and DOCX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents use Simplified Chinese labels and are written to local output paths; the skill may also return structured JSON from service calls.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata, created 2026-08-18T10:34:19Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
