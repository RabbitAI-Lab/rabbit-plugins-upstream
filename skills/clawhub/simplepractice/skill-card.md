## Description:

Helps clients read appointments, billing records, paperwork, and announcements in their SimplePractice Client Portal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and authorized caregivers use this skill to check upcoming healthcare appointments, portal billing records, outstanding forms, and practice announcements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal responses may expose sensitive medical or billing information, including records for multiple clients under one login.

Mitigation: Confirm the intended client before reporting results, and share only the information the user requested.

Risk: Requesting a sign-in link sends an email and repeated requests may impede access.

Mitigation: Request a new link only with the user's approval and avoid duplicate or repeated requests.

Risk: An empty portal billing list may not reflect bills managed outside the portal.

Mitigation: Describe empty results as no bills shown in the portal, not proof of a zero balance.

## Reference(s):

- [SimplePractice skill on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may contain sensitive medical and billing information; portal reads do not cancel appointments, sign forms, or pay bills.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
