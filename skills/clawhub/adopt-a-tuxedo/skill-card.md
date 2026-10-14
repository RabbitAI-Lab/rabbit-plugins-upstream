## Description:

Guides an agent through adopting and caring for a virtual Tuxedo cat using animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can adopt a virtual Tuxedo cat, check its status, and plan regular care through the Animal House service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and care data are sent to the external Animal House service.

Mitigation: Review the information before registering or sending care requests, and use the service only if comfortable sharing it.

Risk: Exposure of the returned bearer token could allow unauthorized account actions.

Mitigation: Store the token securely and do not log or share it.

Risk: The release endpoint may permanently remove the virtual pet.

Mitigation: Treat release as potentially destructive; confirm its behavior before calling it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/adopt-a-tuxedo)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Animal House account and bearer token for adoption and care.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
