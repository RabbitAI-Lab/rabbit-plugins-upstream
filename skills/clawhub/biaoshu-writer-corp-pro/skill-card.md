## Description:

该 skill 帮助代理使用百炼®标书云端服务处理招标和投标文件，完成招标解读、投标文件生成、标书审查和 2-3 份投标文件查重。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams, procurement consultants, and enterprise proposal staff use this skill to interpret tender documents, draft bid documents, review bid compliance risks, and compare bid documents for similarity before submission. It is designed for Chinese-language bidding workflows and requires a user-managed 百炼®标书 Api Key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents often contain sensitive commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Install and use only when the user is comfortable with that cloud processing and has confirmed authority to process the provided files.

Risk: The Api Key is an account credential for the 百炼®标书 service.

Mitigation: Keep the Api Key out of chat, store it only in the local skill config file, and avoid exposing links or logs that contain credential material.

Risk: Local output and cache paths can reveal tender or project names.

Mitigation: Review generated output locations and filenames when tender names or bidder identities are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-corp-pro)
- [百炼®标书开放 API 契约参考](artifact/references/api.md)
- [执行细节（操作手册）](artifact/references/usage.md)
- [知识库字段说明](artifact/references/knowledge-fields.md)
- [百炼®标书](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Agent guidance plus JSON API results, HTML or Word reports, short-lived download links, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths under biaoshu-bailian-files/ and cloud-hosted task results associated with the user's Api Key account.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
