## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot checks, reservation and favorite listing, and booking, modification, or cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want an agent to produce fpx commands and request bodies for OpenTable workflows without running the OpenTable MCP server. It supports reservation discovery and account actions through the user's own signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to perform real OpenTable booking, modification, cancellation, or favorite changes through a signed-in browser session without an enforced final confirmation step.

Mitigation: Require the agent to present the exact restaurant, date, time, party size, cancellation policy, fees or deposits, and card requirement, then wait for explicit user approval before any write action.

Risk: OpenTable booking flows can include cancellation fees, deposits, credit card requirements, same-day conflicts, 3-D Secure, experience requirements, or regional shard limitations.

Mitigation: Preview booking details and account conflicts before committing, and treat OpenTable errors or missing details as a reason to stop and ask the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable fpx request catalog](artifact/references/opentable-fpx-requests.md)
- [Initial state extraction helper](artifact/references/extract-initial-state.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, jq filters, and Node.js helper usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that perform real OpenTable account actions through the user's signed-in browser session.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
