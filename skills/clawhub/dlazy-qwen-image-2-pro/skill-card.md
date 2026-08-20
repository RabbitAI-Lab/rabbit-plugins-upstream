## Description:

This skill lets agents use dLazy's Alibaba Bailian qwen-image-2.0-pro wrapper to generate images from prompts and up to three reference images, with options for negative prompts, image size, prompt rewriting, dry runs, and asynchronous polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create or iterate images with qwen-image-2.0-pro through the pinned dLazy CLI, including mixed text/image design prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image inputs passed to the skill may be sent to dLazy's hosted service.

Mitigation: Submit only content approved for third-party cloud processing and avoid passing sensitive local files unless that use is authorized.

Risk: Authentication may store or use a dLazy API key on the local machine.

Mitigation: Use the OS-user restricted CLI config or DLAZY_API_KEY intentionally, and rotate or revoke API keys when access is no longer needed.

Risk: The skill depends on a pinned third-party CLI package.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package or source before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration guidance, image URLs]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy authentication, and network access to api.dlazy.com and files.dlazy.com; generated outputs are returned as hosted image URLs or async task IDs.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
