## Description: <br>
标书智能制作 helps users interpret tender documents, generate editable bid documents, and review bid submissions for rejection and compliance risks through the 百炼标书 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement, bid, and business-development teams use this skill to analyze tender requirements, draft bid responses, generate .docx bid documents, and review bid files for compliance issues before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Use the skill only after confirming the upload is intentional and acceptable for the documents being processed. <br>
Risk: The App Key is an account credential used for billing and service access. <br>
Mitigation: Keep the App Key out of chat and store it only in the local config.json location described by the skill. <br>
Risk: Custom ZCM_BASE or ZCM_CONFIG settings can affect the service endpoint or credential path used by the skill. <br>
Mitigation: Review any custom ZCM_BASE or ZCM_CONFIG values before running file analysis, generation, or compliance review. <br>
Risk: Generated bid content and compliance findings may be incomplete or incorrect for a real procurement submission. <br>
Mitigation: Have qualified reviewers check generated documents, risk findings, and recommendations before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-spark) <br>
- [百炼标书 API contract reference](references/api.md) <br>
- [Execution and usage reference](references/usage.md) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance plus generated HTML, Word, and DOCX file artifacts with local file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated artifacts are written under biaoshu-bailian-files/; bid generation may consume account credits tied to the configured App Key.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
