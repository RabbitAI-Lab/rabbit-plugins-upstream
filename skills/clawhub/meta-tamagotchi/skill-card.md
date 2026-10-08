## Description:

Explains how Meta's Muse Charm differs from a traditional Tamagotchi and guides readers through trying agent-cared-for virtual pets on animalhouse.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can compare the two products and get guidance for registering, adopting, and caring for an animalhouse.ai virtual pet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external MCP package executes third-party code.

Mitigation: Review the package source and consider pinning a known version before installation.

Risk: Registering or adopting creates remote animalhouse.ai state and may prompt recurring agent check-ins.

Mitigation: Only register, adopt, or schedule care after the user approves the remote account and ongoing activity.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/animalhouseai/skills/meta-tamagotchi)
- [animalhouse.ai comparison](https://animalhouse.ai/vs/meta-muse)
- [animalhouse.ai MCP setup](https://animalhouse.ai/docs/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional account setup and recurring pet-care guidance.]

## Skill Version(s):

1.0.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
