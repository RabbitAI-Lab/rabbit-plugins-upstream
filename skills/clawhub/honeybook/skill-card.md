## Description:

This skill helps an agent work with HoneyBook client-portal data for wedding-vendor contracts, invoices, proposals, payments, messages, meetings, tasks, and questionnaires.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect HoneyBook portal status, summarize vendor activity, retrieve project and payment details, and prepare controlled portal actions such as sending messages or opening signing and payment links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links, flow links, and cached sessions can function as credentials.

Mitigation: Install and use the skill only when the agent is intended to handle HoneyBook portal links and sessions, and treat pasted portal or flow links as sensitive credential material.

Risk: Message, contract, and invoice workflows can affect real HoneyBook vendors, co-clients, agreements, and payments.

Mitigation: Review previews before sending messages and use confirm:true only when ready to send a real portal message or open signing or payment links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured tool guidance, and inline command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portal deep links, previews for outbound messages, compact summaries, and raw HoneyBook records when requested.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
