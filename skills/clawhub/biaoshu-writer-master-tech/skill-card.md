## Description:

基于百炼®标书开放 API 的技术标生成工具，同一 App Key 也支持招标文件解读与合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret tender documents, generate technical bid documents, and review bid files for compliance risks. It is intended for workflows where users provide local tender or bid files and understand that those files are uploaded to the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business, pricing, and personal data that is uploaded to biaoshu.zhiliaobiaoxun.com.

Mitigation: Confirm user consent before upload and explain that outputs and uploaded files are associated with the user's App Key account.

Risk: The App Key is an account credential and can be exposed if pasted into chat or forwarded in credential-bearing links.

Mitigation: Have the user create config.json locally, never ask them to paste the App Key, and do not forward links that contain key or bind_key parameters.

Risk: Bid generation can consume account credits.

Mitigation: Check and communicate credit requirements before generation, and distinguish balance-gate checks from actual credit-consuming generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-tech)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API Contract Reference](references/api.md)
- [Usage and Execution Guide](references/usage.md)
- [Knowledge Base Field Reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Concise agent replies, structured JSON results, HTML or Word reports, and generated .docx bid files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads user-selected tender or bid files to the stated service, writes local outputs under the configured output directory, and may consume account credits for bid generation.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
