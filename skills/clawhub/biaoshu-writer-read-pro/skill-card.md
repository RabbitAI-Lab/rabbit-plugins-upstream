## Description:

招标文件解析助手使用 App Key 调用百炼®标书开放 API，帮助代理完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting mainland-China bidding workflows use this skill to analyze tender files, generate editable bid documents, and review bid submissions for compliance risks. It is intended for Chinese tender and bid documents handled through the 百炼®标书 cloud API.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential commercial, pricing, or personal data and are uploaded to the 百炼®标书 service for processing.

Mitigation: Review before installing or using the skill, confirm user consent before upload, and avoid processing sensitive documents unless the official service and retention terms are acceptable.

Risk: The skill claims a single official external target, but the API destination can be overridden.

Mitigation: Use only the official API endpoint and do not set ZCM_BASE or login --base unless the destination is fully trusted.

Risk: The App Key is a full account credential stored in a local config file.

Mitigation: Keep the credential local, do not paste it into chat, preserve restrictive file permissions, and rotate the key if exposure is suspected.

Risk: Uploaded files and generated results are retained by the service for a limited period under the App Key account.

Mitigation: Tell users that service-side retention applies and have them manage historical data through the 百炼®标书 platform when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with generated .docx bid files and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts may include tender interpretation reports, editable bid documents, compliance review reports, risk summaries, and absolute output paths.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
