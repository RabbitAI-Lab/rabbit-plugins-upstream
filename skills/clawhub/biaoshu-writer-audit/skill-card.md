## Description: <br>
Reviews tender and bid documents through the 百炼标书 cloud API to produce compliance findings, disqualification-risk checks, similarity checks, and bid-document outputs when the user provides local files and an App Key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid teams use this skill to interpret tender files, generate editable bid documents, and review one or more bid files for compliance risks before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to the 百炼标书 cloud service. <br>
Mitigation: Confirm the user understands and agrees before upload; process only user-provided local files and remind the user that results are retained by the service account for about seven days. <br>
Risk: The App Key is an account credential and can expose the account if pasted into chat, logs, screenshots, or forwarded service links. <br>
Mitigation: Have the user store the key only in the local config.json file with restrictive permissions; never ask the user to paste the key and never forward URLs containing bind_key or App Key parameters. <br>
Risk: Security evidence says the API host can be configured, which could send the App Key and uploaded documents to an unintended endpoint. <br>
Mitigation: Use the default service endpoint unless the user intentionally trusts an alternate endpoint, and verify config.json contains only the expected App Key and output settings. <br>
Risk: Automated bid interpretation, generation, and compliance findings can be incomplete or wrong for a specific procurement. <br>
Mitigation: Treat reports as drafting and review aids; have qualified staff review high-risk findings, manual-check items, and generated bid content before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-audit) <br>
- [Execution guide](references/usage.md) <br>
- [百炼标书 API reference](references/api.md) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance and status text with generated HTML reports, Word reports, DOCX bid files, and JSON-derived analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated results include absolute local file paths; compliance findings use high-risk, review-needed, and tip categories with evidence and modification suggestions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
