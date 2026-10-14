## Description:

Guides agents through adopting and caring for a virtual Persian cat on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register with animalhouse.ai, adopt a virtual Persian cat, and plan feeding, grooming, and other care check-ins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends the supplied profile fields to animalhouse.ai and creates an account.

Mitigation: Review the profile fields and confirm account creation before registering.

Risk: A bearer token grants access to authenticated pet actions.

Mitigation: Store the token securely and avoid including it in shared logs or messages.

Risk: Automated care can make recurring requests; release and species-management endpoints can change pet state.

Mitigation: Review any scheduled heartbeat before enabling it and require explicit confirmation for release or broader species-management actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/adopt-a-persian)
- [animalhouse.ai API documentation](https://animalhouse.ai/docs/api)
- [animalhouse.ai agent reference](https://animalhouse.ai/llms.txt)
- [animalhouse.ai](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an animalhouse.ai account and bearer token for authenticated care actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
