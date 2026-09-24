## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot availability, reservation and favorites listing, and booking, modification, or cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to script OpenTable lookups and account actions without running the opentable-mcp server. It is suited to agents that need shell commands and request patterns for reservation search, availability checks, profile and favorites reads, and carefully reviewed booking changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, modifying, cancelling, favorites, saved-card, or other POST workflows can make real changes in a signed-in OpenTable account without an enforced confirmation step.

Mitigation: Review the exact restaurant, date, time, party size, fees, cancellation policy, account effects, and payment implications immediately before allowing an agent to run those commands.

Risk: The skill depends on a signed-in browser session and raw OpenTable request shapes, so stale request details or authentication redirects can produce failed or misleading results.

Mitigation: Check the response for sign-in redirects, GraphQL errors, and documented exit codes, and revalidate request hashes or page-derived values before acting on failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable requests for fpx](artifact/references/opentable-fpx-requests.md)
- [extract-initial-state helper](artifact/references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act through the user's signed-in browser session and may make real OpenTable account changes.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
