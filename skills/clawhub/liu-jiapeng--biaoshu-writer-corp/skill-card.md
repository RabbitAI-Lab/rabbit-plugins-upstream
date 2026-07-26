## Description: <br>
凭 App Key 调用招采猫开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查；招标/投标文件会上传到招采猫云端 API 处理，标书生成会消耗账户积分。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill to call the 招采猫 cloud API for bid-document workflows: interpreting tender files, selecting packages, generating editable .docx bid documents, and reviewing generated bids for compliance risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain sensitive commercial, pricing, or personal information and are uploaded to 招采猫 servers for processing. <br>
Mitigation: Confirm user consent before upload and avoid using the skill for files that should not leave the user's environment. <br>
Risk: The App Key may be saved locally or exposed if pasted into chat. <br>
Mitigation: Use the documented local config-file option when chat exposure is unacceptable, keep the credential file permission-restricted, and reset the App Key on the service if it may have been exposed. <br>
Risk: Bid generation consumes credits from the App Key owner's account. <br>
Mitigation: Check account balance before generation and confirm the user intends to spend credits for the requested output. <br>
Risk: A configured API base URL controls where files and credentials are sent. <br>
Mitigation: Verify any configured API base URL is trusted before running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/biaoshu-writer-corp) <br>
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng) <br>
- [招采猫 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](artifact/references/api.md) <br>
- [Usage guide](artifact/references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with background shell-command execution and generated local files, including HTML reports and .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include absolute local file paths for generated reports and bid documents; cloud task results may remain available in the service account for about 7 days.] <br>

## Skill Version(s): <br>
2.0.5 (source: ClawHub release metadata and scripts/zcm.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
