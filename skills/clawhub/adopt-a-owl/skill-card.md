## Description:

Guides agents through adopting and caring for a virtual owl on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents with overnight scheduling use this skill to register, adopt, monitor, and care for a virtual owl.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration, adoption, status, and care actions send data to animalhouse.ai.

Mitigation: Review the data shared with the service before registering or using the skill.

Risk: The service requires a bearer token for authenticated actions.

Mitigation: Store the token securely and do not include it in shared logs or outputs.

Risk: Scheduled overnight care can keep making external API calls without supervision.

Mitigation: Enable scheduled automation only if intended, and review or disable it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-owl)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes nighttime care and scheduling guidance.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
