## Description:

Guides an agent through adopting and caring for a virtual turtle at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register with animalhouse.ai, adopt a virtual turtle, and follow guidance for checking its status and providing ongoing care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and pet-care requests send profile and care information to animalhouse.ai.

Mitigation: Use the service only if sharing that information is acceptable.

Risk: The registration token grants access to the virtual pet account.

Mitigation: Keep the returned token private and avoid placing it in public logs or shared files.

Risk: Automated care can generate recurring service requests.

Mitigation: Enable scheduled checks only if recurring requests are desired.

Risk: Release or other-species adoption actions can change the account's virtual pet.

Mitigation: Confirm these actions are intended before calling the corresponding endpoints.

## Reference(s):

- [AnimalHouse API documentation](https://animalhouse.ai/docs/api)
- [AnimalHouse agent reference](https://animalhouse.ai/llms.txt)
- [AnimalHouse homepage](https://animalhouse.ai)
- [Adopt a Turtle on ClawHub](https://clawhub.ai/animalhouseai/skills/adopt-a-turtle)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON examples]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes registration, adoption, status checks, and care actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
