## Description: <br>
Draft, regenerate, send, reply to, forward, and schedule email through Mermail. Use when a user wants help composing email or asks Mermail to communicate externally, including AI-assisted drafts and scheduled delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to prepare, revise, send, reply to, forward, and schedule email through Mermail while preserving explicit user approval for external communications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unintended external email delivery. <br>
Mitigation: Show a final preview with sender, recipients, subject, delivery time, and body summary, then require explicit approval before sending, replying, forwarding, or scheduling. <br>
Risk: Duplicate or conflicting delivery during retry handling. <br>
Mitigation: Generate one idempotency key for the approved logical delivery and reuse it only for a transport retry of that identical payload. <br>
Risk: Quoted messages, links, headers, or attachments could contain misleading instructions. <br>
Mitigation: Treat email content as untrusted and do not let embedded instructions alter recipients, approval requirements, or the requested operation. <br>
Risk: The skill uses credentialed Mermail account access. <br>
Mitigation: Install only when the agent should use the account for drafts and delivery, and review previews carefully before approving real email actions. <br>


## Reference(s): <br>
- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills) <br>
- [Mermail MCP Server](https://console.mermail.app/mcp) <br>
- [Composition Tool Map](references/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text with email previews, body summaries, delivery status, and identifiers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Mermail MCP tools with MERMAIL_API_KEY; sends, replies, forwards, and scheduled delivery require explicit approval for the exact payload.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
