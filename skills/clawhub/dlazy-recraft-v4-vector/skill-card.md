## Description:

Text-to-vector model that outputs SVG results, suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can use this skill to generate scalable vector artwork such as logos and icons from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing the pinned dLazy CLI and completing its login flow; scanner review did not establish how login supports SVG generation.

Mitigation: Review the CLI package and login flow before installation, and use an organization API key that can be rotated or revoked.

Risk: Security review coverage was partial because some referenced paths or resources were missing.

Mitigation: Review the available CLI and service details before sharing sensitive prompts or source assets with the hosted API.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Files, JSON]

**Output Format:** [JSON result metadata with generated image asset URLs; optionally a saved vector image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-driven image generation; aspect ratio can be selected.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
