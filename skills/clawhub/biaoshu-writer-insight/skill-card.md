## Description: <br>
A Chinese bid-writing assistant that uses a 百炼®标书 App Key to interpret tender documents, generate editable .docx bid files, and review submissions for compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users preparing Chinese tender submissions use this skill to analyze procurement files, draft bid documents, and run compliance checks before submission. It is intended for document workflows where users can consent to uploading local tender or bid files to the 百炼®标书 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service. <br>
Mitigation: Confirm user consent before upload and process only user-selected local files. <br>
Risk: The App Key is a full account credential and could leak through chat, logs, or parameterized service links. <br>
Mitigation: Keep the App Key in local config.json only, do not ask the user to paste it, and do not forward links containing bind_key or other credential parameters. <br>
Risk: Generated bid documents and compliance analyses can affect procurement decisions and may contain incomplete or incorrect guidance. <br>
Mitigation: Require user review of generated documents, risk findings, and manual checklists before submission. <br>
Risk: Uploaded files and generated results are retained under the App Key account on the 百炼®标书 service for about seven days. <br>
Mitigation: Tell users about service-side retention and direct them to manage history on the 百炼®标书 platform. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight) <br>
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage and operation guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus locally written .docx, HTML, Word, and JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated bid documents, interpretation reports, and compliance reports are written to local files while results are also available in the service account.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
