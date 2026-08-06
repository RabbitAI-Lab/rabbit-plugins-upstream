## Description: <br>
Manage an Instagram creator or business account through InstantDM tools by triaging and replying to comments, answering DMs, monitoring ad comments, reviewing account and post insights, and working with the linked Facebook Page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanjaykhanssk](https://clawhub.ai/user/sanjaykhanssk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, businesses, and their agents use this skill to manage Instagram engagement through InstantDM, including comment triage, inbox follow-up, ad comment monitoring, lead tagging, and weekly performance reporting. It is intended for workflows where the user reviews and approves outbound messages before they are sent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound replies, DMs, automation triggers, and comment responses reach real people and may spend InstantDM credits. <br>
Mitigation: Show the exact text, exact target, and batch credit cost before sending; send only after explicit user approval. <br>
Risk: Credit exhaustion or hourly limits can interrupt sending workflows. <br>
Mitigation: Stop immediately on 402 or 429 responses, report what was sent and what remains, and do not retry automatically. <br>
Risk: Repeated identical messages to many users can create account-safety and trust risks. <br>
Mitigation: Keep batches small, vary drafts, and avoid mass-sending identical text. <br>
Risk: Private conversation contents may include sensitive user information. <br>
Mitigation: Summarize private threads and avoid pasting long private conversation contents unless the user explicitly asks to see them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanjaykhanssk/skills/instagram-autodm) <br>
- [InstantDM MCP endpoint](https://openapi.instantdm.com/mcp?auth=<key>) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance, draft replies, triage tables, summaries, recommendations, and tool-call plans] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outbound messages require explicit user approval before sending.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
