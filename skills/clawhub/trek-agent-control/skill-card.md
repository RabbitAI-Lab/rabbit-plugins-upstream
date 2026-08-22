## Description:

Trek 微信旅行 Agent lets WorkBuddy and compatible agents research trips, inspect or update Trek mini program itineraries, and safely synchronize structured travel data through an authenticated Trek Agent Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and their agents use this skill to plan travel, inspect Trek trip state, synchronize itinerary places and assignments, upload travel documents, manage reservations, lodging, costs, packing, todos, and collaboration proposals, and run diagnostics against the Trek service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent configured with a Trek Agent Key can access and update the user's Trek trip data.

Mitigation: Use a separate key for this agent, keep it out of shared files and logs, verify the endpoint before configuring it, and revoke the key when the integration is no longer needed.

Risk: Bulk, financial, membership, proposal-decision, rescheduling, or other high-impact writes could change real travel data incorrectly.

Mitigation: Preview high-impact changes, write in small batches, reuse existing entities when possible, and verify persisted state with readback before reporting synchronization complete.

Risk: The agent could introduce unsupported travel facts, booking details, coordinates, or confirmation status.

Mitigation: Use official or primary sources for time-sensitive facts, preserve unresolved items as todos or notes, and mark reservations confirmed only when user or order evidence exists.

Risk: Server schema changes, authentication failures, permission errors, or rate limits can make tool behavior differ from stored documentation.

Mitigation: Run doctor or tools/list before writing, trust fresh server schemas, stop on authentication or permission failures, and handle 429 responses sequentially with bounded retry behavior.

## Reference(s):

- [Runtime configuration](artifact/references/configuration.md)
- [Dynamic tool and field guide](artifact/references/field-guide.md)
- [Research and synchronization workflows](artifact/references/workflows.md)
- [ClawHub skill page](https://clawhub.ai/super21-bat/skills/trek-agent-control)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, MCP configuration examples, tool-call arguments, and JSON checklist examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Trek Agent Key; write operations are expected to use previews, small batches, and readback verification.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
