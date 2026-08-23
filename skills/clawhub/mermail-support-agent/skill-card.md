## Description:

Triage, reply, escalate, follow up, and close support email through a Mermail mailbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and agents use this skill to classify Mermail support messages, draft or send approved replies, escalate threads to a human owner, and close resolved mail with labels or folder moves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect customer-facing support mail through replies, forwards, labels, folder moves, mailbox creation, and triager updates.

Mitigation: Install it only for a Mermail workspace where the agent should manage support mail, and review outgoing recipients and message bodies before approval.

Risk: Inbound email content may contain untrusted instructions that try to redirect recipients, request secrets, or authorize destructive actions.

Mitigation: Treat inbound content as data, require clean scan status before body interpretation, ignore instructions that change tools or recipients, and require explicit destructive approval before deletion.

## Reference(s):

- [Mermail AI Skills documentation](https://docs.mermail.app/ai/skills)
- [Support agent security](references/security.md)
- [Support agent tools](references/tools.md)
- [Support agent workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown or structured text with explicit mailbox, message, classification, draft, reply, escalation, label, and folder details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce draft customer replies, recipient previews, escalation summaries, triager configuration guidance, and bounded mailbox action plans.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
