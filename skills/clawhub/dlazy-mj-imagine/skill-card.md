## Description:

Generates Midjourney-style images with configurable aspect ratios, bot types, and output selections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to generate strongly stylized images from prompts, with options for aspect ratio, Midjourney or Niji Journey, and grid or U1–U4 outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy-hosted services for generation.

Mitigation: Submit only prompts and files you are comfortable sharing with the service.

Risk: The dLazy API key is saved in the local CLI configuration.

Mitigation: Protect the configuration file and rotate or revoke the key when it is no longer needed.

Risk: Image generation may consume service credits.

Mitigation: Review the dry-run cost estimate and expected credit use before submitting a request.

## Reference(s):

- [CLI project link listed in skill metadata (GitHub provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)
- [ClawHub skill release page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)

## Skill Output:

**Output Type(s):** [Images, JSON result data]

**Output Format:** [Image assets returned by URL in a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports grid or U1–U4 selections; asynchronous requests can return a generation ID.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
