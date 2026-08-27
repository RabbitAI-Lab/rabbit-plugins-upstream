## Description:

Generates images with Alibaba Bailian qwen-image-2.0-pro, emphasizing complex text rendering, multi-line layouts, photorealistic detail, semantic adherence, and mixed Chinese/English text-image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Qwen Image 2 Pro image generation from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media files are sent to dLazy's hosted service for generation.

Mitigation: Use only content approved for that service and avoid sending sensitive media unless the user or organization permits it.

Risk: API keys may be saved in the local dLazy CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on installing or running the third-party dLazy CLI.

Mitigation: Use the pinned CLI version from the artifact and review the linked source or npm package before installing in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or save generated image files when --save is used; async mode returns a task identifier.]

## Skill Version(s):

1.3.9 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
