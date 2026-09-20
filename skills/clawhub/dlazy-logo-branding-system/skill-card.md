## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and brand teams use this skill to plan a logo and brand identity workflow, generate core mark concepts, and extend approved marks into variants, social assets, and brand system deliverables through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any user-provided image, video, or audio inputs may be sent to dLazy-hosted services.

Mitigation: Use the skill only with data appropriate for third-party processing, and avoid sending confidential brand assets unless that use is approved.

Risk: Using dLazy login or auth setup can store an API key in the local dLazy configuration file.

Mitigation: Use DLAZY_API_KEY per session when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The evidence notes documentation version inconsistencies around the dLazy CLI and skill release.

Mitigation: Confirm the intended skill and CLI versions before publishing, installing globally, or relying on the documented commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with structured requirements summaries, prompt drafts, status updates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs returned by dLazy-hosted services.]

## Skill Version(s):

1.2.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
