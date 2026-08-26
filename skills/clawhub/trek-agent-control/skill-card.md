## Description:

Connects an agent to the Trek WeChat travel mini program so it can research trips, inspect Trek data, synchronize itinerary details, upload tickets, run diagnostics, and safely update trips through an authenticated remote MCP service or CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to let WorkBuddy, Codex, Claude, OpenClaw, Hermes, or another compatible agent plan travel and synchronize structured trip data back to the user's Trek workspace. It is suited for itinerary creation, trip updates, candidate-place voting, reservations, accommodations, costs, packing, todos, attachments, collaboration notes, and connection diagnostics when the user provides a Trek Agent Key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify real Trek trip data through a user-provided Trek Agent Key.

Mitigation: Install it only when that access is intended, use a separate Trek Agent Key for the agent, store the key in a secret manager when possible, and revoke the key if it is exposed.

Risk: Destructive, financial, reservation, proposal-decision, rescheduling, or bulk changes could materially alter a user's travel plan.

Mitigation: Review concrete previews before those changes, write in small batches, and verify results with Trek readback before reporting synchronization complete.

Risk: Incorrect trip facts, locations, prices, opening hours, or booking status could be synchronized into the travel workspace.

Mitigation: Use current primary or official sources for time-sensitive facts, preserve uncertainty as todos or notes, and avoid marking reservations confirmed without order evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/super21-bat/skills/trek-agent-control)
- [Runtime configuration](references/configuration.md)
- [Dynamic tool and field guide](references/field-guide.md)
- [Research and synchronization workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, MCP configuration snippets, and structured change previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include readback summaries, diagnostics, unresolved facts, and user confirmation requirements before high-risk writes.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
