## Description: <br>
从招标解读直达成标的编制工具。它读懂招标文件的评分与废标要求后，一键生成成品投标文件(.docx)、编排投标应答，并完成合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid teams use this skill to interpret tender documents, generate editable bid documents, and review bid files for compliance risks before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain sensitive business, pricing, or personal information and are uploaded to the 百炼标书 service for processing. <br>
Mitigation: Confirm user awareness and consent before upload, and process only files the user explicitly provides for this purpose. <br>
Risk: The App Key grants account access and could be exposed if pasted into chat or stored carelessly. <br>
Mitigation: Keep the key in the local config file, keep that file private, and never ask the user to paste or repeat the key in conversation. <br>
Risk: Changing the configured service endpoint could send documents or credentials to an untrusted destination. <br>
Mitigation: Use the stated 百炼标书 endpoint unless the user has a trusted, intentional override. <br>
Risk: Generated bid documents and compliance findings may be incomplete or unsuitable for final submission without review. <br>
Mitigation: Have qualified staff review generated documents, risk findings, and recommendations before filing or relying on them. <br>


## Reference(s): <br>
- [API contract reference](references/api.md) <br>
- [Usage guide](references/usage.md) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown responses plus local HTML, Word, and DOCX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated bid documents and compliance reports should be reviewed by a human before filing.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
