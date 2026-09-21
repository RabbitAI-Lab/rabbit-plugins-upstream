## Description:

Generate high-quality images with Vidu Q2, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Q2 image-generation service from an agent workflow. It supports prompt-driven image generation, optional reference images, asynchronous execution, and saving generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be sent to dLazy's hosted service.

Mitigation: Avoid sensitive prompts or local files unless the user is comfortable uploading them to dLazy.

Risk: The CLI stores a dLazy API key in local user configuration when authenticated.

Mitigation: Use per-invocation environment variables or rotate and revoke keys from the dLazy dashboard when access should change.

Risk: API calls may consume account credits and generated assets are hosted by dLazy.

Mitigation: Use the dry-run or npx path for review before persistent installation or credit-consuming execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as hosted URLs and can be saved locally with the CLI.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
