## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images through the dLazy CLI using Doubao Seedream 4.5 from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local images may be sent to dLazy services for generation.

Mitigation: Avoid submitting sensitive prompts or local files unless they are intended for dLazy processing.

Risk: Persistent login stores an API key in the local dLazy configuration file.

Mitigation: Prefer per-command DLAZY_API_KEY when possible, check permissions on ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI and hosted API for image generation.

Mitigation: Review the pinned CLI package and source before installation, and use dry-run or npx invocation when evaluating behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing generated image URLs and may save image files locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous and asynchronous generation, optional image references, 2k or 4k resolution, common aspect ratios, and dry-run cost estimation.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
