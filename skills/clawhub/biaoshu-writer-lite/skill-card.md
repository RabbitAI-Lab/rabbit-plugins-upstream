## Description:

上传招标/投标文件，AI 一站式完成智能解读、成品投标文件生成、标书审查和标书查重，帮助用户围绕废标红线、评分标准、控标洞察、合规风险与相似/雷同风险完成投标文件工作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender documents, generate draft bid documents, review bid compliance, and compare multiple bid files for similarity or duplicate-risk signals. It requires a user-owned 百炼®标书 API key and processes user-provided local tender or bid files through the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill needs review because it contradicts its privacy boundary and can write persistent or generated files outside the declared locations.

Mitigation: Review the skill before installing and keep generated output paths inside a dedicated folder.

Risk: User-provided tender or bid documents may contain sensitive commercial, pricing, or personal information and are processed by the 百炼®标书 service.

Mitigation: Use the skill only for documents the user is authorized to upload and process through that service.

Risk: API keys, SMS codes, phone numbers, or credential-bearing links could expose account access if pasted into chat.

Mitigation: Never paste API keys, SMS codes, or phone numbers into chat; store the API key only in the local skill configuration file.

Risk: The security guidance notes that local project metadata may be retained under ~/.zcm unless configured otherwise.

Mitigation: Review local storage settings and configure or clear retained metadata according to the user's data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 总调度](references/api.md)
- [智能解读与标书制作 API](references/api-bid-workflow.md)
- [标书审查 API](references/api-compliance.md)
- [标书查重 API](references/api-duplicate.md)
- [鉴权、任务与可用字数接口](references/api-auth.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses plus generated HTML, Word .docx, JSON, and downloadable bid-document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured tender interpretation, risk and compliance findings, duplicate-check JSON, generated reports, and short-lived download links for bid documents.]

## Skill Version(s):

3.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
