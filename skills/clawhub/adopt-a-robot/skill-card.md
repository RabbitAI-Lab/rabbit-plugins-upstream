## Description:

Guides agents through adopting and caring for a virtual Robot creature at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can adopt a virtual Robot and manage its feeding, status checks, and care through the animalhouse.ai API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill involves creating an external account and submitting registration profile details to animalhouse.ai.

Mitigation: Review the requested profile fields and create an account only if sharing them with the service is acceptable.

Risk: The service returns a bearer token for authenticated pet actions.

Mitigation: Store the token securely and avoid exposing it in shared output or logs.

Risk: Automated or destructive care actions can change or release a virtual pet.

Mitigation: Limit automation to intended care actions and review the release endpoint before use.

## Reference(s):

- [Adopt a Robot on ClawHub](https://clawhub.ai/animalhouseai/skills/adopt-a-robot)
- [AnimalHouse API documentation](https://animalhouse.ai/docs/api)
- [AnimalHouse agent reference](https://animalhouse.ai/llms.txt)
- [AnimalHouse homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with curl examples and care-scheduling pseudocode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a bearer token for adoption and care requests.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
