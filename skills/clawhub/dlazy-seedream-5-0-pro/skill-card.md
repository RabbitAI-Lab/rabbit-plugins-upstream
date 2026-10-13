## Description:

Helps agents generate detailed, typography-conscious images for commercial visuals and brand assets using Seedream 5.0 Pro through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to request commercial key visuals and brand images from a prompt, optionally with reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files are sent to dLazy's hosted service.

Mitigation: Only provide prompts and files you are comfortable uploading to dLazy.

Risk: Installing the third-party CLI or saving an API key locally may not suit every environment.

Mitigation: Confirm you trust the CLI and service before installation; use npx for on-demand execution and DLAZY_API_KEY for per-run credentials instead of storing a key locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI commands; the CLI returns JSON with image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images, aspect ratio, asynchronous generation, and local result download.]

## Skill Version(s):

1.2.24 (source: ClawHub release; bundled CLI instructions specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
