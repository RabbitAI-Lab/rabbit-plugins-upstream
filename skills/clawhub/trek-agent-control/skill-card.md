## Description:

Helps travel-planning agents research destinations, manage Trek itineraries, and sync structured trip details to the Trek mini program.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and their agents use this skill to plan trips, inspect existing Trek data, and synchronize itineraries, reservations, expenses, and attachments to a shared trip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read and modify live trip data across a broadly authorized Trek account.

Mitigation: Use a separate revocable Trek Agent Key, preview changes, verify updates, and revoke the key when finished.

Risk: A generic Trek call may invoke destructive actions without the batch confirmation flow.

Mitigation: Avoid generic calls for writes; confirm high-impact operations with the user before executing them.

Risk: Uploading local files can disclose sensitive tickets or other personal documents to Trek.

Mitigation: Upload only files the user explicitly intends to share with the Trek service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/super21-bat/skills/trek-agent-control)
- [Configuration guide](references/configuration.md)
- [Travel workflows](references/workflows.md)
- [Trek field guide](references/field-guide.md)
- [Cross-midnight scheduling](references/cross-midnight.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown and text with commands and structured trip updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May synchronize live trip records and upload attachments when authorized.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
