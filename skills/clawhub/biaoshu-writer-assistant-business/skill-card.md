## Description:

基于百炼®标书开放 API，帮助用户解读招标文件、生成商务标投标文件并进行合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队、商务标撰写人员和招投标顾问可用此 skill 处理中国大陆招投标文件：上传本地招标或投标文件后，获取结构化解读、商务标 .docx 草稿和合规审查报告。首次上传前应确认用户知悉文件会发送至百炼®标书云端处理。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the third-party 百炼®标书 service for processing.

Mitigation: Confirm user awareness and consent before the first upload, and process only files the user explicitly provides.

Risk: The App Key is an account credential that can authorize API actions and account-credit use.

Mitigation: Keep the App Key out of chat, store it only in the local config.json file, and do not forward URLs that contain key-bearing parameters.

Risk: Generating bid documents consumes credits from the App Key owner's account.

Mitigation: Precheck the account balance and make the credit-consuming generation step clear before submitting it.

Risk: Changing the API base could send sensitive tender data to an unintended endpoint.

Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user explicitly trusts and approves an alternate endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-business)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Chinese-language assistant responses plus generated HTML reports, Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local App Key configuration file and writes generated artifacts to the configured output directory.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
