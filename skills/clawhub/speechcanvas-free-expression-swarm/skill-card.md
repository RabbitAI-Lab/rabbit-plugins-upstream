## Description:

A free-expression image-prompt swarm with Muse, Guardian, Critic, and Composer roles, a JSON prompt schema, a safety validator pattern, and a refinement loop for lawful civic, journalism, protest, and censorship-themed imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative agents use this skill to turn lawful civic-expression briefs into structured image prompt packs, with built-in checks against fake evidence, real-person deception, harassment, and unsafe crisis imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts could be misleading if symbolic civic imagery is turned into fake evidence, fake documents, real-person deception, or crisis imagery.

Mitigation: Review generated prompts before use and keep the documented constraints for no fake evidence, no official seals, no real public figures, no private targets, and no readable instructions.

Risk: Optional external image-generation tools could move prompt content outside the local workspace.

Mitigation: Use no network by default, enable external tools only when the operator explicitly chooses them, and keep filesystem access scoped to the working directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/speechcanvas-free-expression-swarm)
- [ClawHub publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Structured JSON prompt packs with Markdown guidance, safety tags, review notes, and final image-generation instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for human review before any optional image-generation service is used.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
