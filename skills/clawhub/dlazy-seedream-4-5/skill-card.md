## Description:

Generates images from text prompts or reference images with Doubao Seedream 4.5 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users generate images from text or transform reference images using the dLazy-hosted Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images are sent to a third-party service.

Mitigation: Avoid submitting sensitive prompts or images unless approved for dLazy processing.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials or use the per-invocation environment variable option.

Risk: Broad image-generation requests can consume paid credits.

Mitigation: Confirm generation requests and check the CLI cost estimate with --dry-run when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, Shell commands, Configuration guidance]

**Output Format:** [JSON CLI response containing image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image, selectable resolution and aspect ratio, and asynchronous jobs.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
