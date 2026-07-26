## Description: <br>
WeChat AI assistant for proactive messaging and automated replies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cool131219](https://clawhub.ai/user/cool131219) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
WeChat users can ask an agent to send a direct message to a named contact or read visible chat context and prepare an AI-generated reply. The skill is intended for desktop WeChat automation where the operator is comfortable granting message-reading and message-sending authority. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read visible WeChat chat content, including private conversations. <br>
Mitigation: Use it only on chats the operator is authorized to access and review what content may be processed before invoking auto-reply. <br>
Risk: OCR.space use may involve third-party processing of private chat content. <br>
Mitigation: Avoid sensitive chats or substitute an approved OCR path when third-party processing is not acceptable. <br>
Risk: The skill can send messages on the user's behalf with weak user-control safeguards. <br>
Mitigation: Require explicit operator review of generated replies before running commands that send messages. <br>
Risk: The published artifact appears to omit scripts that the skill text says are bundled. <br>
Mitigation: Verify the required scripts are present and reviewed before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cool131219/skills/reply-wechat-message) <br>
- [Server-resolved GitHub provenance](https://github.com/cool131219/WeChat-Butler/tree/main/reply-wechat-message) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured conversation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include contact names, message text, and structured chat context labels.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
