## Description:

Guides agents through adopting and caring for a virtual chameleon on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to register with Animal House, adopt a virtual chameleon, and manage its ongoing care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and care send user-provided data to an external service, and care requests require a bearer token.

Mitigation: Use only if comfortable sharing that data with Animal House; store the bearer token securely.

Risk: Scheduled care may perform ongoing actions without user review.

Mitigation: Enable recurring care only with explicit user approval.

Risk: The care timing guidance is inconsistent, and releasing a pet is a consequential action.

Mitigation: Confirm timing against the service response and call the release endpoint only when explicitly intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/adopt-a-chameleon)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes adoption, status-checking, and care instructions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
