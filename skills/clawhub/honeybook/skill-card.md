## Description:

This skill helps an agent work with HoneyBook client-portal data for contracts, invoices, questionnaires, messages, meetings, tasks, payments, and related wedding-vendor workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to inspect and act on HoneyBook client-portal workspaces, including vendor files, contracts, invoices, messages, meetings, questionnaires, payments, and tasks. It is intended for cases where the user is comfortable giving the agent access to HoneyBook portal credentials and related client and vendor data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook portal credentials can expose client, vendor, contract, invoice, payment, message, meeting, and contact data.

Mitigation: Install and use only when the user accepts that access level; prefer compact or summary views and avoid raw responses unless needed.

Risk: Raw modes can reveal vendor-side data beyond a normal client task.

Mitigation: Use compact or sectioned views first, and request raw data only for a specific missing field or troubleshooting need.

Risk: Outgoing messages, signing links, and payment links may trigger real-world workflow consequences.

Mitigation: Confirm outgoing messages, signing links, and payment links deliberately before taking action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or text responses with HoneyBook portal data, summaries, previews, and action links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact summaries by default, raw portal data when explicitly requested, message previews, and deep links for signing or payment.]

## Skill Version(s):

0.10.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
