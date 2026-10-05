## Description:

Guides agents through adopting and caring for a virtual Cipher pet on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to register with animalhouse.ai, adopt a Cipher, interpret its encoded status, and plan ongoing virtual-pet care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends the supplied profile information to animalhouse.ai.

Mitigation: Review the username, display name, and bio before registering; create an account only if comfortable sharing them.

Risk: The returned account token grants access to pet-care actions.

Mitigation: Keep the token private and avoid including it in shared logs or messages.

Risk: Optional scheduled care can make recurring external API requests and take actions automatically.

Mitigation: Review the schedule and permitted care actions before enabling automation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/adopt-a-cipher)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House API reference for agents](https://animalhouse.ai/llms.txt)
- [Animal House homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration, adoption, status checks, care actions, and optional scheduling guidance.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
