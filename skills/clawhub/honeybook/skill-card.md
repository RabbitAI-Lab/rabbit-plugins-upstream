## Description:

This skill helps an agent work with HoneyBook client-portal data for wedding-vendor contracts, invoices, questionnaires, messages, meetings, tasks, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to review HoneyBook client-portal content, track vendor obligations, retrieve contract and invoice links, inspect questionnaires, and prepare or send portal messages with confirmation for actions that change state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores persistent HoneyBook portal credentials and can access private client-portal content.

Mitigation: Install and use it only when the user is comfortable granting that access, and keep credentials scoped to the intended HoneyBook portal sessions.

Risk: Raw views may expose vendor-side account or email data unrelated to the immediate task.

Mitigation: Prefer compact or task-specific sections, and request raw views only when a needed field is unavailable elsewhere.

Risk: Messages, contract signing, and payment flows can affect real HoneyBook workflows.

Mitigation: Use preview or deep-link behavior first and require explicit confirmation before sending messages, signing contracts, or paying invoices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text with HoneyBook portal summaries, message previews, status details, and deep links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirmation; raw views may expose broader portal data than the immediate task needs.]

## Skill Version(s):

0.10.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
