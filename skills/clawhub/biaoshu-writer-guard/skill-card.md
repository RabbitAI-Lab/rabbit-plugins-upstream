## Description: <br>
A bid-document writing agent skill that uses a local App Key to call the 百炼®标书 API for tender interpretation, bid document generation, compliance review, and similarity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams, procurement consultants, and business developers use this skill to interpret tender files, draft editable .docx bid submissions, and review bid documents for rejection risks before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial or personal information and are uploaded to the 百炼®标书 service for processing. <br>
Mitigation: Confirm the user understands and agrees to the upload before running interpretation, generation, or compliance review tasks. <br>
Risk: The App Key authorizes use of the user's account and should not be exposed in chat or logs. <br>
Mitigation: Store the key only in the local config file with restrictive permissions, keep it out of conversation, and review any legacy ~/.zcm credential fallback before use. <br>
Risk: Bid document generation consumes credits from the App Key account. <br>
Mitigation: Check balance and confirm credit use before starting generation. <br>
Risk: Generated bids and compliance findings may affect business or legal submission decisions. <br>
Mitigation: Have a qualified human review generated documents, risk findings, and required edits before filing a bid. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard) <br>
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage and operation guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus generated local HTML, Word, JSON, and .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files are written locally under the configured output directory, while API results are associated with the user's App Key account.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
