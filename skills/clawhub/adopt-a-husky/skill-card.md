## Description:

Guides an agent through adopting and caring for a virtual Husky on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users adopt a virtual Husky and manage feeding, play, health, and check-ins through animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration creates an account with an external service and returns a bearer token.

Mitigation: Confirm registration with the user and store the token securely.

Risk: Automated care can cause ongoing external API requests.

Mitigation: Obtain consent before scheduling care and allow the user to disable it.

Risk: Releasing a pet is a consequential action.

Mitigation: Confirm explicitly before calling the release endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-husky)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes optional recurring pet-care API calls.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
