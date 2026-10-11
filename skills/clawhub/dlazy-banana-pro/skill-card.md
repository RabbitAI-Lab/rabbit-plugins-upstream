## Description:

Generates and edits images with Nano Banana Pro from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from text prompts and reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image files are sent to dLazy's hosted service.

Mitigation: Avoid supplying private images or sensitive prompts unless you intend to share them with dLazy.

Risk: Generation requests may consume account credits.

Mitigation: Check the cost estimate with dry-run before submitting a request.

Risk: The dLazy API key is stored by the CLI for subsequent requests.

Mitigation: Protect the local key and rotate or revoke it when necessary; use an environment variable for per-request access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown guidance and JSON image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally when requested.]

## Skill Version(s):

1.2.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
