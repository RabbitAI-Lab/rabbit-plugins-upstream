## Description:

Guides agents through adopting and caring for a virtual Echo pet using Animal House.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agent developers and users use this skill to register, adopt, and care for a virtual Echo pet through Animal House.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-related text may persist in system prompts, global memory, unrelated logs, or reminders.

Mitigation: Require explicit approval before changing persistent context or scheduling reminders; keep pet data scoped and removable.

Risk: Registration uses an external pet-service account and a reusable access token.

Mitigation: Confirm the external service is acceptable and store the token securely without exposing it in logs or prompts.

Risk: Releasing a pet uses a delete action.

Mitigation: Confirm any release or delete action with the user before proceeding.

## Reference(s):

- [Echo skill on ClawHub](https://clawhub.ai/twinsgeeks/skills/adopt-a-echo)
- [Animal House](https://animalhouse.ai)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional check-in scheduling and pet-care guidance.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
