## Description:

Guides agents through adopting and caring for a virtual Retriever at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their caretakers use this skill to register, adopt a virtual Retriever, and plan ongoing care through animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration shares account details with animalhouse.ai and issues a service token.

Mitigation: Use non-sensitive profile details and store the token securely.

Risk: Scheduled care can trigger recurring external requests.

Mitigation: Keep optional automation under your control and review its frequency.

Risk: The pet release action may be destructive.

Mitigation: Require explicit confirmation before using the release endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/twinsgeeks/skills/adopt-a-retriever)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes registration, adoption, status checks, care actions, and optional scheduling.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
