## Description:

Guides agents through adopting and caring for a virtual Lab dog at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their caretakers use this skill to adopt a virtual Lab, monitor its condition, and plan ongoing care through Animal House.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration creates an external Animal House account and returns a bearer token.

Mitigation: Store the token securely and avoid sharing it or including sensitive personal information in profile fields or care notes.

Risk: Scheduled care can make recurring requests to Animal House.

Mitigation: Enable scheduled calls only if you are comfortable with ongoing external requests, and review the schedule before activation.

Risk: Releasing the virtual pet is destructive.

Mitigation: Confirm intent before calling the release endpoint.

## Reference(s):

- [Adopt a Lab on ClawHub](https://clawhub.ai/twinsgeeks/skills/adopt-a-lab)
- [Animal House](https://animalhouse.ai)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent documentation](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scheduled care guidance]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
