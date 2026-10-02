## Description:

Helps clients read appointments, billing, paperwork, payment methods, and announcements in their SimplePractice Client Portal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and their authorized representatives use this skill to check portal appointments, balances, billing records, pending forms, and practice announcements without changing portal records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A portal login may cover multiple clients, exposing another family member's sensitive health or billing information.

Mitigation: Confirm the intended client record before reporting details, and disclose only information the user requested.

Risk: The saved portal session can remain available after the conversation ends.

Mitigation: Sign out when the user no longer wants the portal session available.

Risk: Repeated sign-in link requests may trigger address or IP rate limits.

Mitigation: Check the existing session and inbox first; request a new link only with the user's confirmation.

Risk: An empty portal billing list may be mistaken for proof that no payment is owed.

Mitigation: Describe only what the portal shows and avoid drawing conclusions about bills issued elsewhere.

## Reference(s):

- [SimplePractice skill on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain-language responses or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal information; detail depends on the signed-in client's records and permissions.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
