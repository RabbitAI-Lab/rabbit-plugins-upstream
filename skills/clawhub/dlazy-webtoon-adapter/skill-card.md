## Description:

Adapts web novels into webtoon plot breakdowns and episode scripts, with a separate dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use this skill to turn web-novel chapters into serialized webtoon outlines and episode scripts. It also offers a dLazy-powered image-generation workflow when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The writing workflow also directs agents to install or run the dLazy CLI and generate images, which may be unexpected.

Mitigation: Review the full skill before installation and confirm that CLI-based image generation is intended for the task.

Risk: CLI authentication stores an API key locally, and prompts or selected local media may be sent to dLazy services.

Mitigation: Protect and rotate the API key, and review prompts and media before sending or uploading them.

Risk: The release version and versions cited within the skill differ, making the installed CLI version unclear.

Mitigation: Confirm the intended skill and CLI versions before installing or executing commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Conversational Markdown with structured plot breakdowns and episode scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts target 500–800 characters per episode; image generation can return hosted image URLs after user confirmation.]

## Skill Version(s):

1.3.24 (source: server release metadata; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
