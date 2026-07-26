## Description: <br>
This skill helps agents use the Biaoshu bid-document API to interpret tender files, generate editable bid documents, and run optional compliance reviews on bid submissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user wants to analyze tender requirements, create a bid document, or review one or more bid documents for compliance risks. It is intended for bid-writing workflows where the user explicitly provides local tender or bid files and understands they will be processed by the Biaoshu cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files can contain commercial, pricing, and personal information and are uploaded to the Biaoshu cloud API for processing. <br>
Mitigation: Confirm the user understands and agrees before uploading files, and process only files the user explicitly provides for this workflow. <br>
Risk: The Biaoshu App Key is an account credential and generated bid documents can consume account credits. <br>
Mitigation: Keep the App Key out of chat, store it only in the local configuration file, and confirm account balance before credit-consuming generation. <br>
Risk: Generated bid documents and compliance findings may be incomplete or need business and legal judgment before submission. <br>
Mitigation: Have qualified reviewers inspect generated documents, evidence, and risk findings before relying on them for a live bid. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review) <br>
- [Biaoshu service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [Biaoshu API contract reference](references/api.md) <br>
- [Execution and usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Conversation guidance plus local files such as .docx bid documents, HTML reports, and optional Word reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a locally stored Biaoshu App Key and user-selected local tender or bid files; generated bid documents can consume account credits.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
