## Description:

This skill helps agents work with HoneyBook client-portal data, including vendor contracts, invoices, questionnaires, messages, meetings, tasks, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with HoneyBook client-portal access use this skill to let an agent inspect wedding-vendor workspace data, summarize status, retrieve messages and meetings, and prepare portal actions such as signing, paying, or replying. Actions that can affect portal state require explicit confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links, flow links, cached portal sessions, and flow credentials can grant access to sensitive HoneyBook data.

Mitigation: Install only when HoneyBook portal-session access is intended, treat pasted links as credentials, and keep cached session files protected.

Risk: Signing contracts, paying invoices, and sending messages can affect real vendor workflows.

Mitigation: Review returned previews and use confirmation only after checking the target workspace, message, contract, or invoice.

Risk: Requests about invoices, payments, or vendor replies may refer to another service or workspace.

Mitigation: Ask the agent to clarify ambiguous requests before allowing HoneyBook actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, API Calls, guidance]

**Output Format:** [Markdown or structured text returned by agent tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HoneyBook portal deep links, compact summaries, raw record views, message previews, and confirmation-gated action results.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
