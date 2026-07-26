## Description: <br>
Uses an App Key to call the 百炼®标书 cloud API to analyze tender documents, generate editable bid documents, and optionally review bid compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and bid-writing users use this skill to interpret tender files, generate editable bid submissions, and review bid files for compliance after acknowledging cloud upload, retention, and billing implications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain business or personal data and are uploaded to the 百炼®标书 cloud service for processing. <br>
Mitigation: Confirm user consent before upload and review the service's retention terms before using confidential bid materials. <br>
Risk: The App Key is a full account credential for the external service. <br>
Mitigation: Keep the App Key out of chat, store it only in the local config file, and avoid forwarding links that contain key or bind_key parameters. <br>
Risk: Generated bid documents and compliance reports can affect procurement decisions. <br>
Mitigation: Review generated documents, high-risk findings, manual checklists, and any remaining placeholders before submission. <br>
Risk: Bid-document generation consumes credits from the App Key owner's account. <br>
Mitigation: Check balance and confirm the user wants to proceed before starting credit-consuming generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance, JSON API results, HTML or Word reports, and .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated reports and bid documents to a local output directory; requires a locally stored App Key and user-selected tender or bid files.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
