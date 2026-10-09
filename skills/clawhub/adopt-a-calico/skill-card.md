## Description:

Guides agents through adopting and caring for a virtual Calico cat at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and their caretakers use this skill to register, adopt a virtual Calico, check its status, and plan ongoing care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends the selected username, display name, and bio to animalhouse.ai.

Mitigation: Review profile fields before registration and share only information intended for that service.

Risk: The account token grants access to pet-care actions.

Mitigation: Store the returned token securely and avoid exposing it in logs or shared output.

Risk: Scheduled care can make repeated authenticated requests; releasing a pet is destructive.

Mitigation: Limit automation to status and care actions, and require explicit confirmation before release.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-calico)
- [Animal House](https://animalhouse.ai)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.4 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
