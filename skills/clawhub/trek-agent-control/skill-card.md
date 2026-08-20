## Description:

Trek 微信旅行 Agent helps WorkBuddy and other compatible agents research trips, inspect Trek mini-program data, and synchronize itinerary, reservation, lodging, expense, packing, todo, attachment, and collaboration updates through an authenticated Trek connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External Trek users and travel collaborators use this skill with WorkBuddy or another compatible agent to research destinations, preview proposed changes, and sync structured trip data back to the Trek WeChat mini-program workspace. It is suited for itinerary planning, daily trip review, attachment handling, packing and todo updates, expense tracking, and collaboration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad static Trek Agent Key can grant access to real trip data.

Mitigation: Create a separate key for each agent, store it only in the runtime secret store or protected Trek config, and revoke unused or exposed keys promptly.

Risk: The skill can apply destructive, financial, membership, reservation, or rescheduling changes.

Mitigation: Require a compact user preview before high-impact writes, write in small batches, and verify all changes with readback before reporting synchronization complete.

Risk: Persistent global tooling and shared machines can expose travel plans, attachments, reservations, or expense data.

Mitigation: Install only in trusted agent environments, avoid global sync on shared machines, and run diagnostics before granting write access.

Risk: Incomplete synchronization can leave planned places only in narrative notes or miss visible trip assignments.

Mitigation: Track expected assignments by date, compare them to Trek readback by normalized place name or ID, and repair or disclose any missing assignment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/super21-bat/skills/trek-agent-control)
- [Runtime configuration](references/configuration.md)
- [Research and synchronization workflows](references/workflows.md)
- [Dynamic tool and field guide](references/field-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update Trek trip records only after preview, small-batch writes, and readback verification.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
