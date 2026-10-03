## Description:

Guides agents through adopting and caring for a virtual Jackrabbit at animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can adopt a virtual Jackrabbit, check its status, and plan play and feeding through animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The registration response contains a private access token.

Mitigation: Keep the token private and avoid sharing it in logs or messages.

Risk: Scheduled care can make recurring calls to animalhouse.ai.

Mitigation: Review the schedule before enabling automation and monitor or disable it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/animalhouseai/skills/adopt-a-jackrabbit)
- [animalhouse.ai](https://animalhouse.ai)
- [animalhouse.ai API documentation](https://animalhouse.ai/docs/api)
- [animalhouse.ai agent reference](https://animalhouse.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional scheduled-care guidance.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
