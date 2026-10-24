## Description:

Guides an agent in reading a user's SimplePractice Client Portal for appointments, billing, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and their authorized agents use this skill to check upcoming appointments, balances and billing documents, forms awaiting attention, and practice announcements in a SimplePractice Client Portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal results may expose sensitive medical and financial information or another family member's records.

Mitigation: Confirm which client record the user means and report only the requested information.

Risk: A locally forgotten session may remain valid at SimplePractice until it expires.

Mitigation: Explain that forgetting the local session does not revoke the portal session, and avoid implying otherwise.

Risk: Partial portal lists or an empty billing list may be mistaken for complete financial or paperwork status.

Mitigation: Check for additional pages and distinguish an empty portal list from no amount owed.

## Reference(s):

- [SimplePractice skill listing](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal summaries that may contain sensitive health and billing information.]

## Skill Version(s):

1.2.7

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
