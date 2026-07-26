## Description: <br>
智标领航投标文件自动生成 helps users interpret tender files, generate editable bid documents, and review bid compliance through the BaiLian bid-document cloud service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and bid teams use this skill to process local tender files, draft bid documents, and review completed bids for compliance. It is intended for users who can authorize upload of tender and bid materials to the named BaiLian cloud service under their own App Key account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user consent before each upload and use the skill only for documents the user is authorized to send to that service. <br>
Risk: The App Key authorizes the user's BaiLian account and can expose paid operations if shared in chat or URLs. <br>
Mitigation: Have the user create the local config file themselves, never ask them to paste the App Key into chat, and avoid forwarding links that contain key or bind_key parameters. <br>
Risk: Bid-document generation consumes the App Key account's points. <br>
Mitigation: Check account balance before paid generation and confirm with the user before submitting paid document-generation work. <br>
Risk: Generated reports and bid documents are written locally and may include sensitive tender material. <br>
Mitigation: Write outputs only to the declared output directory or a user-selected path, and provide full paths so the user can manage the files. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-express) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [BaiLian bid-document service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, terminal progress text, JSON API responses, HTML or Word reports, and .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated bid documents and reports are written to biaoshu-bailian-files/ by default; operations use a local App Key configuration and the named BaiLian API endpoint.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
