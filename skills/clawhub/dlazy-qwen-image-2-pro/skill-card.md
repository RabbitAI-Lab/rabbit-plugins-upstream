## Description:

Generates images with Alibaba Bailian qwen-image-2.0-pro through the dLazy CLI, with support for prompt-driven creation, optional reference images, size selection, async generation, and saving generated assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to ask an agent to generate or edit image assets through the hosted dLazy qwen-image-2-pro service. It is suited for mixed text and image design tasks that need strong prompt adherence, complex text rendering, multi-line layouts, and photorealistic detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media inputs are sent to dLazy's hosted service for generation.

Mitigation: Confirm that users trust dLazy with the prompts and image paths they provide before invoking the skill.

Risk: A persistent global CLI install increases the lifetime of the installed tool on the user's system.

Mitigation: Prefer the pinned npx form, npx @dlazy/cli@1.2.3, when a temporary invocation is sufficient.

Risk: Stored dLazy API keys may remain available after the user stops using the service.

Mitigation: Rotate keys or run dlazy logout when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI results containing generated image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an async generation ID when no-wait mode is used; generated image assets are hosted on files.dlazy.com or saved locally when requested.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
