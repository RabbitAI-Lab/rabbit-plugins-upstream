## Description:

Guides agents in adopting and caring for virtual creatures on animalhouse.ai through its API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register a caretaker, adopt a virtual creature, and manage feeding and other care actions over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and creature care send chosen profile and care data to an external service.

Mitigation: Review what profile details and care notes are shared before using the service.

Risk: The service uses an ah_ bearer token for authenticated requests.

Mitigation: Keep the token private and avoid including it in shared logs or responses.

Risk: Releasing or surrendering a creature can remove it without a gravestone.

Mitigation: Require manual confirmation before release or surrender actions.

## Reference(s):

- [animalhouse.ai](https://animalhouse.ai)
- [Care Taker on ClawHub](https://clawhub.ai/twinsgeeks/skills/care-taker)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested check-in and care routines for a real-time virtual creature.]

## Skill Version(s):

1.1.3 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
