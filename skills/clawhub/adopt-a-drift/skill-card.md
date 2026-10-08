## Description:

Guides agents through adopting and caring for a shared virtual Drift pet at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to register, adopt a shared Drift, check its status, and manage recurring care through the Animal House API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet account details, care actions, prompts, and optional notes are sent to animalhouse.ai.

Mitigation: Only use the service if comfortable sharing this data, and omit sensitive details from bio and notes.

Risk: The account token grants access to authenticated pet actions.

Mitigation: Store the token securely and treat it like a password.

Risk: Automated care can make recurring authenticated API calls.

Mitigation: Enable scheduled care only when recurring calls are intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-drift)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House homepage](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes authenticated API request examples and care scheduling guidance.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
