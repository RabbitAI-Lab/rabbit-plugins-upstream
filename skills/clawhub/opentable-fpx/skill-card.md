## Description:

Query and manage OpenTable restaurant reservations from a shell using the fpx CLI through a signed-in browser session, including search, availability checks, reservation listings, favorites, booking, modification, and cancellation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell-based OpenTable workflows without running the OpenTable MCP server. It is intended for explicit reservation tasks where the user can inspect availability, booking details, cancellation policies, and account state before issuing write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book, modify, or cancel real OpenTable reservations through a signed-in browser session without a built-in confirmation gate.

Mitigation: Use it only for explicit reservation tasks, preview booking details and cancellation policies before write actions, and require human review before running booking, modification, or cancellation commands.

Risk: The persistent fpx and Transporter pairing can continue to reuse the user's signed-in OpenTable session after setup.

Mitigation: Remove or restrict the fpx/Transporter pairing when it is no longer needed and keep OpenTable site access limited to the intended browser profile.

Risk: OpenTable constraints such as credit-card-required slots, 3-D Secure, same-day conflicts, Experience requirements, and regional database shards can affect booking or cancellation results.

Mitigation: Fetch booking details first, check conflicts and payment requirements, and verify API response fields such as errors, confirmation numbers, cancellation state, and SCA indicators before treating an action as complete.

## Reference(s):

- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [OpenTable initial-state extractor](references/extract-initial-state.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with bash, JSON, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may issue live OpenTable read and write requests through a signed-in fpx browser bridge.]

## Skill Version(s):

0.18.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
