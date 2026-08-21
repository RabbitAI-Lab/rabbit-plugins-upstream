## Description:

基于百炼®标书开放 API 的技术标写作助手，同一 App Key 也支持招标文件解读与合规审查；当用户明确提供招标文件并要求起草技术标、完善技术响应、生成技术标投标文件(.docx)时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users working on mainland-China bidding workflows use this skill to interpret tender files, generate technical bid documents, and review bid documents for compliance through the 百炼®标书 cloud service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal data and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm the user is comfortable uploading the files before use and avoid processing documents that are not permitted to leave the local environment.

Risk: The App Key is a credential for the user's 百炼®标书 account and may expose account access or billing if shared.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and reset it through the platform if exposure is suspected.

Risk: Bid-document generation consumes points from the account tied to the App Key.

Mitigation: Review account balance and point usage before generating bid documents.

Risk: Generated proposals and compliance findings may be incomplete or require business judgment before submission.

Mitigation: Review generated documents, unresolved placeholders, compliance findings, and manual-check items before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-tech)
- [执行细节（操作手册）](artifact/references/usage.md)
- [百炼®标书开放 API 契约参考](artifact/references/api.md)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown/text responses plus generated HTML, Word, and .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are primarily zh-CN and include full local paths for generated artifacts; bid generation may consume account points.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
