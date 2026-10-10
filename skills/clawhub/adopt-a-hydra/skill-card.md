## Description:

Guides agents in adopting and caring for a virtual Hydra pet at animalhouse.ai, including feeding, status checks, and care after it splits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to register for a virtual pet, adopt a Hydra, and manage its ongoing care, including separate care for each creature after it splits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and pet care send profile and pet-care data to animalhouse.ai.

Mitigation: Review what will be shared and obtain user consent before registering or sending care details.

Risk: The service issues a bearer token for account and pet-care actions.

Mitigation: Store the token securely and do not expose it in shared logs or messages.

Risk: Optional automated care can make recurring service calls.

Mitigation: Enable scheduling only with user approval, and review or disable the schedule when care is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-hydra)
- [Animal House](https://animalhouse.ai)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides pet-care steps and optional recurring check-in guidance.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
