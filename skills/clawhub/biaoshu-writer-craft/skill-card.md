## Description: <br>
Consumes tender files and helps produce compliant bid documents by interpreting requirements, drafting technical and commercial bid content, exporting .docx files, and reviewing rejection and compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid-writing teams use this skill to analyze tender files, generate editable bid documents, and review bid submissions for compliance and rejection risk through the named bid-writing service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain confidential commercial, pricing, or personal information and are uploaded to the named service for processing. <br>
Mitigation: Confirm the user understands and agrees to each upload before running interpretation, bid generation, or compliance review. <br>
Risk: Bid document generation can use the App Key account and may consume paid credits. <br>
Mitigation: Check account balance before submission and confirm paid generation steps with the user. <br>
Risk: The App Key is an account credential. <br>
Mitigation: Have the user store it only in the local config file and never paste it into chat or expose links containing the key. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus generated .docx, HTML, and Word report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated bid documents and reports are written to local output paths; some cloud results may expire after about 7 days.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
