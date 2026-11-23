## Description:

Midjourney-style image generation with selectable aspect ratios, bot types, and output positions (grid/U1–U4), for artistic and strongly stylized creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative developers use this skill to request Midjourney-style images from a prompt, choosing an aspect ratio, Midjourney or Niji bot, and grid or U1–U4 output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a benign verdict with medium confidence and partial analysis; it says the supplied commands focus mainly on authentication and the referenced CLI behavior was not established.

Mitigation: Review the linked CLI package and verify its behavior before installing or using it.

Risk: The skill documentation says prompts go to dLazy's hosted API and supplied local media is uploaded to its media storage.

Mitigation: Avoid sending sensitive prompts or media unless sharing them with the hosted service is appropriate.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON result envelope containing output URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt with optional aspect ratio, bot type, and grid/U1–U4 selection; optional asynchronous task ID or local save path.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
