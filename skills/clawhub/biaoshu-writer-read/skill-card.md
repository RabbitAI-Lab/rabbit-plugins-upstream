## Description: <br>
Uses a user-provided App Key to call the BaiLian bid-document API for tender interpretation, package extraction, bid document generation, and optional compliance review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid teams use this skill to upload local tender and bid files to BaiLian's cloud API, receive structured tender analysis, generate editable .docx bid documents, and review completed bids for compliance issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user consent before upload and avoid using the skill for files that should not leave the user's environment. <br>
Risk: The App Key controls the user's service account and billing credits. <br>
Mitigation: Keep the App Key out of chat, store it only in the local config.json, and review custom ZCM_CONFIG or ZCM_BASE settings before use. <br>
Risk: Bid generation can consume account credits. <br>
Mitigation: Check the account balance before generation and confirm before starting paid bid-generation tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read) <br>
- [BaiLian bid document service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Conversational guidance plus generated HTML, Word, and .docx files from API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write reports and generated bid documents under biaoshu-bailian-files/ and uses a local config.json for the App Key.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
