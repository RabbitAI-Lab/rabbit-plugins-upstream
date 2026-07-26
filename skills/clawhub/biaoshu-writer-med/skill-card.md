## Description: <br>
以提分为目标的投标文件写作助手，可解读招标文件、生成投标文件，并对投标文件做合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bidding and proposal teams use this skill to process local tender files, draft bid responses aligned to scoring criteria, produce editable .docx bid documents, and review submitted bid documents for compliance risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial, pricing, or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm the user understands and agrees before uploading files, and do not use the skill for documents that cannot be sent to that service. <br>
Risk: The App Key can consume account credits and access account data if exposed. <br>
Mitigation: Keep the App Key out of chat, store it only in the local config file with restricted permissions, and reset it on the platform if exposure is suspected. <br>
Risk: Custom API base settings can redirect sensitive files and credentials to a nonstandard endpoint. <br>
Mitigation: Use the default service endpoint unless the user explicitly trusts and intends the custom endpoint. <br>
Risk: Generated bid documents and compliance findings may affect commercial submissions if accepted without review. <br>
Mitigation: Have qualified proposal staff review generated content, scoring alignment, required fill-ins, and compliance findings before submission. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/dragonzu/skills/biaoshu-writer-med) <br>
- [招采猫平台](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage and operations guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Chat guidance and progress updates, structured analysis summaries, local HTML or Word reports, and generated .docx bid documents.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include absolute local file paths for generated reports and bid documents.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
