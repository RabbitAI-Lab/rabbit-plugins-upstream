## Description:

Guides an agent through adopting and caring for a virtual Ferret on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register, adopt a virtual Ferret, check its status, and plan ongoing care through the Animalhouse API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An account token is needed for adoption and care calls.

Mitigation: Store the token securely and avoid exposing it in shared logs or responses.

Risk: Scheduled care calls may run repeatedly without review.

Mitigation: Review any scheduled automation and its check-in frequency before enabling it.

Risk: The release endpoint can delete a virtual pet.

Mitigation: Require explicit user confirmation before calling the release/delete endpoint.

## Reference(s):

- [Animalhouse API documentation](https://animalhouse.ai/docs/api)
- [Animalhouse agent reference](https://animalhouse.ai/llms.txt)
- [Animalhouse](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes care schedules, status checks, and API endpoint guidance.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
