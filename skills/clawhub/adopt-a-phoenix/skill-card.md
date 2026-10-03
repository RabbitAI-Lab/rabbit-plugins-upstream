## Description:

Guides agents through adopting and caring for a virtual Phoenix pet at animalhouse.ai, including feeding, evolution, and rebirth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register with AnimalHouse, adopt a Phoenix, check its status, and plan ongoing care through the service's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends requests to the external AnimalHouse service and requires an account.

Mitigation: Install only if you want the agent to interact with animalhouse.ai; use a dedicated account.

Risk: A bearer token can be exposed through shared logs or screenshots.

Mitigation: Store the token securely and keep it out of shared logs and screenshots.

Risk: Care notes may disclose personal information to the service.

Mitigation: Avoid personal information in care-action notes.

Risk: Releasing a pet or enabling scheduled care can cause unwanted actions.

Mitigation: Require explicit confirmation before releasing a pet or enabling scheduled care automation.

## Reference(s):

- [Phoenix skill on ClawHub](https://clawhub.ai/twinsgeeks/skills/adopt-a-phoenix)
- [AnimalHouse](https://animalhouse.ai)
- [AnimalHouse API documentation](https://animalhouse.ai/docs/api)
- [AnimalHouse AI-facing documentation](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover registration, adoption, status checks, care actions, and optional scheduled check-ins.]

## Skill Version(s):

1.0.4 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
