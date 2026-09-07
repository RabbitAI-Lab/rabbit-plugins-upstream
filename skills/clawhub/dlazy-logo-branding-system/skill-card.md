## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and agents use this skill to plan and generate logo concepts, derivative assets, and brand identity system materials through a stepwise dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party dLazy CLI and API key for execution.

Mitigation: Verify the intended @dlazy/cli version before installing, prefer npx or an isolated install, and use a revocable dLazy API key.

Risk: Prompts and supplied media may be uploaded to dLazy API and file services.

Mitigation: Only provide prompts or media that are acceptable to process through dLazy services, and avoid sensitive or confidential assets unless approved.

Risk: Global installation can leave persistent tooling and credentials on the local system.

Mitigation: Use npx for on-demand execution when possible and review the local dLazy configuration file for stored credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline shell commands and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires staged user confirmation before image generation; generated prompts and media are sent to dLazy services.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
