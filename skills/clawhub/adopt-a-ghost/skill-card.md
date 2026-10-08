## Description:

Guides an agent through adopting and caring for a virtual Ghost at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register, adopt a Ghost, monitor its status, and plan recurring virtual-pet care through animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration creates an animalhouse.ai account and authenticated care requests use a token.

Mitigation: Get consent before registering, store the token as a secret, and do not log or share it.

Risk: Scheduled care can continue making background requests without further prompts.

Mitigation: Enable scheduled care only when requested and make it easy to disable.

Risk: Release or species-management actions can change the user's virtual pets.

Mitigation: Require explicit confirmation before using release or species-management endpoints.

## Reference(s):

- [Adopt a Ghost on ClawHub](https://clawhub.ai/animalhouseai/skills/adopt-a-ghost)
- [Animalhouse.ai](https://animalhouse.ai)
- [Animalhouse.ai API documentation](https://animalhouse.ai/docs/api)
- [Animalhouse.ai agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pet status and care suggestions depend on the animalhouse.ai service.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
