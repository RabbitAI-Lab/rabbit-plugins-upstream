## Description:

Trek Agent Control helps WorkBuddy and other agents use an authenticated Trek Agent Key to research travel, inspect Trek trip data, and safely synchronize itinerary, reservation, budget, packing, todo, attachment, and proposal updates back to the Trek mini program.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent plan travel, read current Trek trip state, preview proposed changes, and write structured itinerary data back to the Trek mini program with readback checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs mutable global CLI code and connects to a third-party Trek service.

Mitigation: Install only if the Trek service and publisher are trusted; prefer a pinned release or verified package over the mutable branch install, and confirm the exact endpoint and commands before setup.

Risk: A persistent Trek Agent Key can grant broad access to read and modify real trip data.

Mitigation: Create a separate key for each agent, store it only in a runtime secret manager or protected config, and revoke it when no longer needed or if exposed.

Risk: Agent writes can affect reservations, costs, deletes, proposal decisions, and schedule changes.

Mitigation: Use the skill's previews, confirmation steps, small batches, and readback checks before allowing high-impact writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/super21-bat/skills/trek-agent-control)
- [Runtime configuration](references/configuration.md)
- [Dynamic tool and field guide](references/field-guide.md)
- [Research and synchronization workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include change previews, diagnostics, and readback checks before or after writes.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
