## Description: <br>
Gmail Lead Desk helps agents connect Gmail through the AISA gateway, scan unread sales and support leads, summarize threads, draft replies, and archive messages with labels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadocs](https://clawhub.ai/user/aisadocs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and customer support teams use this skill to triage Gmail inquiries, prepare CRM-ready summaries, draft follow-up messages, and archive completed deals while keeping sends and batch actions under explicit user control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses Gmail through AISA and may handle sensitive mailbox content. <br>
Mitigation: Install only when that access is acceptable, require AISA_API_KEY and OAuth setup, and avoid attachment uploads or downloads unless the user explicitly asks. <br>
Risk: Email sends can reach unintended recipients or send unreviewed content. <br>
Mitigation: Use draft-first workflows, show To/Cc/subject/body before sending, and send only after explicit user confirmation. <br>
Risk: Batch label or archive actions can modify many messages at once. <br>
Mitigation: Show a sample of message IDs and the total count before batch actions, confirm label IDs, and keep delete and filter tools disabled unless explicitly requested. <br>


## Reference(s): <br>
- [Gmail Lead Desk on ClawHub](https://clawhub.ai/aisadocs/skills/gmail-lead-desk-aisa-one) <br>
- [AISA](https://aisa.one) <br>
- [Connect Gmail and execute tools](references/connect_and_execute.md) <br>
- [Gmail Lead Desk Workflows](references/workflows.md) <br>
- [Gmail API Gotchas](references/gmail_gotchas.md) <br>
- [Gmail Tool Whitelist (MVP)](references/tool_whitelist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Gmail workflow tables, email draft previews, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and Gmail OAuth before Gmail API actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
