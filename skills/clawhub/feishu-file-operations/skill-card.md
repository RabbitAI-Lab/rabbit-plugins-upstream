## Description: <br>
Guides agents through sending files to Feishu conversations and creating or writing Feishu cloud documents with OpenClaw CLI or Feishu Bot API workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songweisong](https://clawhub.ai/user/songweisong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to send approved files to Feishu recipients and create or update Feishu cloud documents. It supports both a simplified OpenClaw CLI path and direct Feishu Bot API calls for more controlled integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files or document links may be sent to the wrong Feishu recipient. <br>
Mitigation: Verify the recipient ID or chat ID before sending and confirm the file or document is approved for that audience. <br>
Risk: Feishu app secrets and tenant access tokens can be exposed through shell history, logs, or chat transcripts. <br>
Mitigation: Use approved secret handling, avoid pasting credentials into shared transcripts, and clear or avoid shell history for token commands. <br>
Risk: Sensitive or personal data may be included in uploaded files or generated documents. <br>
Mitigation: Review file and document contents before upload and share only data that is authorized for the target Feishu workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songweisong/skills/feishu-file-operations) <br>
- [Feishu Open Platform](https://open.feishu.cn/) <br>
- [Feishu send message API](https://open.feishu.cn/document/server-docs/im-v1/message/create) <br>
- [Feishu document API](https://open.feishu.cn/document/server-docs/docs/docx-v1/document) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides Feishu API request examples, permission requirements, token guidance, and troubleshooting notes; it does not execute API calls by itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
