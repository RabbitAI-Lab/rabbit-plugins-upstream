## Description:

HoneyBook helps agents work with HoneyBook client-portal data including contracts, invoices, questionnaires, messages, meetings, tasks, notes, attachments, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to review HoneyBook vendor portal content, track contracts and invoices, read questionnaires and messages, inspect meetings and tasks, and prepare confirmed portal actions such as sending messages or opening signing and payment links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links and flow links may grant access to sensitive contracts, invoices, questionnaires, messages, and payment-related data.

Mitigation: Paste portal or flow links only when intentionally authorizing access, and keep cached session files private.

Risk: Sending a message through HoneyBook can email vendors and co-clients in the workspace.

Mitigation: Review the message preview first and use confirm:true only after the content and recipients are correct.

Risk: Signing and payment flows involve consequential portal actions.

Mitigation: Use returned deep links deliberately and require explicit confirmation before requesting signing or payment actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Structured text and portal deep links returned through MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HoneyBook portal data, message previews, meeting details, payment status, and action links that require user confirmation before sensitive actions.]

## Skill Version(s):

0.9.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
