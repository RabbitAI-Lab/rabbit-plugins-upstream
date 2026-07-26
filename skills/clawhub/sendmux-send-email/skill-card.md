## Description: <br>
Send one or many emails through Sendmux using approved mailbox or agent credentials, idempotency keys, attachments, MCP, CLI, SDKs, or HTTP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and send outbound email through Sendmux, including single messages, batch sends, idempotent retries, and attachment workflows. It is intended for workflows where the user has supplied or confirmed recipients, sender details, message content, and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sendmux credentials can be exposed if pasted into chat, command output, logs, screenshots, or shared files. <br>
Mitigation: Use scoped Sendmux credentials stored in environment variables or a secret manager, and avoid printing or pasting secrets. <br>
Risk: An agent could send email to the wrong recipients or with unintended content if message details are incomplete or assumed. <br>
Mitigation: Require the user to supply or confirm every recipient, sender, subject, and message body before sending, including the full set for batch sends. <br>
Risk: Attachments may upload local files to Sendmux for delivery. <br>
Mitigation: Review selected files before upload, use attachment-specific workflows for local files, and avoid sending sensitive files unless the user explicitly approves. <br>
Risk: Retrying a send without idempotency can create duplicate outbound email. <br>
Mitigation: Use one stable Idempotency-Key per logical email or batch whenever a send may be retried. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-send-email) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>
- [Sendmux Sending API endpoint](https://smtp.sendmux.ai/api/v1/emails/send) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, TypeScript snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Sendmux request bodies, idempotency-key guidance, attachment handling steps, CLI, SDK, MCP, or direct HTTP examples.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
