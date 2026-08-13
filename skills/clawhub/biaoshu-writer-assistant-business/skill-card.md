## Description:

基于百炼®标书开放 API 的商务标写作助手，支持招标文件解读、商务标投标文件生成和合规审查，并提示用户文件会上传至百炼®标书云端处理、标书生成会消耗积分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill for mainland-China tender workflows: interpreting tender documents, generating editable commercial bid documents, and reviewing bid files for compliance risks after confirming cloud upload and credit usage.

### Deployment Geography for Use:

Mainland China workflows

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential commercial, pricing, or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload and limit inputs to the user-provided local files needed for the task.

Risk: The App Key is a full account credential stored locally in config.json.

Mitigation: Have the user write the key locally, never request or echo it in chat, and keep the credential file permission-limited.

Risk: Bid generation consumes account credits, and long-running generation can continue after a client interruption.

Mitigation: Check balance before generation, explain credit use, and continue existing jobs instead of resubmitting generation tasks.

Risk: Uploaded files and generated results remain on the third-party service for about seven days under the App Key account.

Mitigation: Tell users about retention before upload and direct them to manage history in the service account when needed.

Risk: Changing the API base URL could send sensitive documents to a different endpoint.

Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user intentionally configures a trusted endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-business)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Conversational guidance plus generated HTML or Word reports and editable .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and platform labels primarily use Simplified Chinese for mainland-China bidding workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
