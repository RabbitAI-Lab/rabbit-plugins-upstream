## Description:

Reads a SimplePractice client portal to help users review appointments, billing records, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and authorized caregivers use this skill to review appointments, billing records, outstanding paperwork, and practice announcements in a SimplePractice client portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal results can reveal sensitive healthcare and billing information, including records for more than one person on the same login.

Mitigation: Confirm whose record is being discussed and share only the requested information with authorized users.

Risk: Requesting sign-in links sends real, rate-limited email and repeated requests can impede access.

Mitigation: Check for an existing session or email first, obtain confirmation before sending, and avoid repeated requests.

Risk: An empty portal billing list can be mistaken for a zero balance when a practice bills outside the portal.

Mitigation: State only that no billing records appear in the portal; do not infer that nothing is owed.

## Reference(s):

- [SimplePractice skill listing on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries of read-only portal records; may contain sensitive healthcare and billing information.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
