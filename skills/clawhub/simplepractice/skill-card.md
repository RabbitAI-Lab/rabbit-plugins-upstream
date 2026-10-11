## Description:

Helps users read their SimplePractice Client Portal for appointments, billing, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and their authorized agents use this skill to check upcoming appointments, balances, invoices, superbills, requested forms, and announcements in a SimplePractice Client Portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected portal exposes sensitive healthcare and billing information.

Mitigation: Connect only with the user's permission and report only the requested person's relevant information.

Risk: A local session may remain available after use, and forgetting it does not revoke the portal session.

Mitigation: Use a trusted server, protect access to its session, and do not treat local sign-out as remote revocation.

Risk: A page-limited result or empty portal billing list may be mistaken for a complete account history.

Mitigation: Check for additional pages and distinguish missing portal records from a zero balance.

## Reference(s):

- [SimplePractice skill listing](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries of portal records; some lists and counts cover only the newest page.]

## Skill Version(s):

1.2.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
