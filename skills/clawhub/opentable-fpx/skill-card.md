## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot availability checks, reservations and favorites review, and booking, modifying, or cancelling tables through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to query OpenTable data and manage reservations from shell workflows through a signed-in browser session. It supports searching restaurants, checking available slots, listing reservations or favorites, and performing booking, modification, favorite-change, or cancellation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real OpenTable bookings, modifications, favorite changes, and cancellations through a signed-in browser session without a built-in confirmation gate.

Mitigation: Require explicit human confirmation before write actions, preview booking details and cancellation policies first, and treat reservation tokens, saved-card identifiers, email, and phone data as sensitive.

## Reference(s):

- [OpenTable requests for fpx](artifact/references/opentable-fpx-requests.md)
- [extract-initial-state.mjs](artifact/references/extract-initial-state.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable](https://www.opentable.com)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that can perform real account actions through a signed-in browser session.]

## Skill Version(s):

0.16.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
