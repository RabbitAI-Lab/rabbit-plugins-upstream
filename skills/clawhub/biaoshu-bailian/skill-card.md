## Description: <br>
百炼标书智能写作工具 helps agents use the 百炼®标书 API to interpret tender documents, extract bid packages, generate editable .docx bid documents, and optionally review compliance after user consent to upload files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid-writing teams use this skill to turn local tender files into interpretation reports, generated bid documents, and compliance review reports. It is intended for workflows where users understand that tender and bid files are uploaded to the 百炼®标书 service and bid generation may consume account credits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain sensitive business, pricing, or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user awareness and consent before the first upload, and only process files the user explicitly provides. <br>
Risk: The App Key is an account credential that could expose account access if pasted into chat or forwarded in credential-bearing links. <br>
Mitigation: Keep the App Key in the local config file, do not ask users to paste it into chat, and do not forward URLs containing bind_key or other credential parameters. <br>
Risk: Bid generation consumes credits from the App Key owner's account. <br>
Mitigation: Check balance before generation and make the credit impact clear before submitting generation tasks. <br>
Risk: Changing service endpoints or credential paths can redirect sensitive files or credentials to an untrusted destination. <br>
Mitigation: Use the default service endpoint and local credential path unless the user explicitly trusts the replacement location. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-bailian) <br>
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [百炼®标书 API reference](references/api.md) <br>
- [Usage guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files, Configuration] <br>
**Output Format:** [Markdown guidance plus generated .docx, .html, and Word report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tender interpretation summaries, generated bid documents, compliance findings, local report paths, and account-balance guidance.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata and release changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
