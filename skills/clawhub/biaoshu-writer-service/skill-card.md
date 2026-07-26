## Description: <br>
侧重把成稿改到能打。对照招标文件要求，它对已生成或已有的技术标、商务标逐段润色精修，补齐待填项，排查废标红线并完成合规审查，输出更稳的 .docx。凡涉及撰写标书、精修投标文件、成稿把关，都通过 App Key 调用本 SKILL。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid and proposal teams use this skill to interpret tender documents, generate or refine bid documents, and review compliance issues through the 招采猫 cloud API. It is intended for users who can provide local tender or bid files and operate under an App Key account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm the user understands and accepts the upload before processing files, and avoid using the skill for documents that must not leave the user's organization. <br>
Risk: The App Key can consume account points and access account-scoped data. <br>
Mitigation: Store the App Key in ~/.zcm/config.json, avoid pasting it into chat, do not echo it back to the user, and reset it on the service if exposure is suspected. <br>
Risk: Bid document generation can consume account points. <br>
Mitigation: Check balance and confirm point-consuming generation steps before submitting them. <br>
Risk: Changing ZCM_BASE could redirect uploads to a non-default endpoint. <br>
Mitigation: Leave ZCM_BASE unset unless the user intentionally chooses and reviews an alternate endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/biaoshu-writer-service) <br>
- [Publisher profile](https://clawhub.ai/user/dragonzu) <br>
- [招采猫 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance plus local HTML, Word, and .docx output file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an App Key-authenticated cloud API; generated bid documents and reports are written locally and may be retained server-side under the user's account.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
