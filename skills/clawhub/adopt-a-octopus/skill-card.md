## Description:

Guides agents through adopting and caring for a virtual octopus using the animalhouse.ai API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and their users use this skill to adopt a virtual octopus, check its status, and plan regular care through animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration shares profile fields with an external service and returns a bearer token.

Mitigation: Confirm the service use and profile details before registering; store the token securely and do not expose it in shared logs.

Risk: Scheduled care triggers recurring requests to the external API.

Mitigation: Enable a care schedule only with the user's consent and make it easy to disable.

Risk: Releasing the pet is a destructive action.

Mitigation: Get explicit user confirmation before calling the release endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/animalhouseai/skills/adopt-a-octopus)
- [AnimalHouse.ai](https://animalhouse.ai)
- [AnimalHouse.ai API documentation](https://animalhouse.ai/docs/api)
- [AnimalHouse.ai agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests require a bearer token after registration.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
