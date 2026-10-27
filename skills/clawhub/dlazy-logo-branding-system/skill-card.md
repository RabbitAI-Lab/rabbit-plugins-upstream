## Description:

Guides users through planning a logo and brand visual system and generating image assets with dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Brand designers and teams use this skill to plan logo concepts, build a consistent visual identity system, and generate related image assets through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference assets may be sent to dLazy services for generation.

Mitigation: Share only prompts and reference assets you are comfortable sending to dLazy.

Risk: The API key is stored in the user's local dLazy configuration unless supplied through the documented environment-variable option.

Mitigation: Protect the local configuration and rotate or revoke the key through the dLazy dashboard if needed.

Risk: The skill includes a stale CLI version reference that differs from its stated installation version.

Mitigation: Confirm the intended CLI version before installation; the release guidance identifies 1.2.3 as the install version and 1.0.9 as stale.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Design guidance]

**Output Format:** [Logo concepts, design rationales, and generated brand-identity image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive, staged workflow with user confirmation before image generation.]

## Skill Version(s):

1.2.29 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
