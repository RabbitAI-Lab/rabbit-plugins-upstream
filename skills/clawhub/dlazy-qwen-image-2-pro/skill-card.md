## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layouts, photorealistic detail, semantic adherence, and mixed Chinese-English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call dLazy's hosted Qwen Image 2 Pro image-generation service from the CLI, producing image result URLs or saved image assets from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local image or media paths passed to the CLI are sent to the dLazy hosted service, and generated outputs are hosted by dLazy.

Mitigation: Avoid sending sensitive prompts or files unless dLazy's service terms and data handling are acceptable for the use case.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication when a saved local key is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the pinned third-party @dlazy/cli package and the dLazy hosted service.

Mitigation: Install only after accepting the pinned CLI package and hosted-service dependency; use the documented npx invocation to avoid a persistent global binary when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [JSON responses with image URLs, optional saved image files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, async task IDs, polling, prompt rewriting, image references, and selectable output sizes.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
