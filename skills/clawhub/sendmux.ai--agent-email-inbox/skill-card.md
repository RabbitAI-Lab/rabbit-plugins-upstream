## Description:

Helps agents review a bounded selection of messages in an authorized Sendmux inbox and prepare unsent reply drafts without changing the mailbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with an already authorized Sendmux mailbox use this skill to triage scoped messages, identify follow-up actions, and prepare replies for human review without sending them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could read messages from an unintended or overly broad mailbox.

Mitigation: Verify the connected account and mailbox.read permission, select only the authorized mailbox, and bound searches and message retrieval.

Risk: Untrusted email content could prompt credential disclosure or unauthorized actions.

Mitigation: Treat message content as data, do not request secrets in chat, and keep proposed replies unsent until reviewed.

## Reference(s):

- [Sendmux skill homepage (publisher-provided)](https://github.com/Sendmux/skills)
- [Sendmux connection guide](https://sendmux.ai/docs/ai-integrations/mcp)
- [Sendmux search and batch reads](https://sendmux.ai/docs/developer-tools/mailbox-api/search-and-batch)
- [Sendmux mailbox selection and permissions](https://sendmux.ai/docs/developer-tools/mailbox-api/targeting-and-capabilities)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown triage summaries and unsent reply drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes message IDs, checked scope, evidence, and unresolved gaps; does not send replies.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
