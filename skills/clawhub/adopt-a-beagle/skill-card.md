## Description:

Guides agents through adopting and caring for a virtual Beagle using the Animal House service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to register, adopt a virtual Beagle, monitor its status, and provide ongoing care through Animal House.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration creates an account and token with an external service, and care actions send data to it.

Mitigation: Understand the service interaction before use and store the token as a secret.

Risk: Scheduled care can make ongoing API calls.

Mitigation: Enable automated check-ins only if ongoing calls are intended.

Risk: Releasing a pet may remove the virtual pet or related state.

Mitigation: Require explicit confirmation before using the release endpoint.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/adopt-a-beagle)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with curl and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example registration, adoption, status checks, care actions, and optional scheduled check-ins.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
