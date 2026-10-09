## Description:

Helps users read their SimplePractice Client Portal for appointments, billing, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and their authorized representatives use this skill to check appointments, balances, billing records, paperwork, and announcements in a practice's client portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected portal access can expose sensitive healthcare and billing information, including records for multiple clients under one login.

Mitigation: Confirm whose record is requested, share only necessary details, and sign out when the session should not be reused.

Risk: Repeated sign-in emails may trigger portal rate limits and interrupt access.

Mitigation: Check for an existing session or email first, request user confirmation before sending a sign-in link, and avoid repeated requests.

## Reference(s):

- [SimplePractice skill on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal summaries; compact responses by default for supported reads.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
