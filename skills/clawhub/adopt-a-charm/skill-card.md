## Description:

Guides agents through adopting and caring for a virtual Charm pet on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can adopt a virtual Charm pet, check its status, and plan recurring care through the AnimalHouse service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account profile and pet-care data are sent to a third-party service.

Mitigation: Review the data shared with animalhouse.ai before creating an account or using the skill.

Risk: The returned bearer token grants access to account and pet-care actions.

Mitigation: Store the token securely and avoid exposing it in shared logs or output.

Risk: Automated care makes recurring authenticated calls that can change the pet's state.

Mitigation: Enable scheduled care only after reviewing its frequency and permitted actions.

## Reference(s):

- [Adopt a Charm on ClawHub](https://clawhub.ai/animalhouseai/skills/adopt-a-charm)
- [AnimalHouse API documentation](https://animalhouse.ai/docs/api)
- [AnimalHouse agent reference](https://animalhouse.ai/llms.txt)
- [AnimalHouse homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and care-scheduling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested authenticated API requests for adoption, status checks, and pet care.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
