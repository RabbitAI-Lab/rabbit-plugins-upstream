## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to invoke the dLazy CLI for Seedream 4.5 image generation from text prompts or reference images, with options for resolution, aspect ratio, async generation, and saving generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, generation parameters, and selected local image inputs to dLazy cloud endpoints for inference and media handling.

Mitigation: Pass only prompts and files intended for upload, and review cloud/API use with the user's data-handling requirements.

Risk: Authentication depends on a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use a scoped and revocable API key, rotate it when needed, and prefer per-invocation environment variables in shared or temporary environments.

Risk: A global CLI installation can persist third-party executable code on the user's system.

Mitigation: Prefer pinned on-demand execution with npx or a contained environment unless a global install is intentionally required.

Risk: The save option writes generated assets to a user-provided local path.

Mitigation: Choose explicit output paths and inspect saved files before reusing them in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional saved image files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
