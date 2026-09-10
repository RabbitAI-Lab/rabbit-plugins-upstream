## Description:

Generate images with the Kling o1 model from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images through the dLazy CLI using Kling Image O1, including text-to-image and image-to-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local files may be uploaded to dLazy services for cloud image generation.

Mitigation: Avoid submitting private prompts or images unless the user is comfortable uploading them to dLazy.

Risk: The skill depends on a third-party npm CLI and dLazy account credentials.

Mitigation: Review the linked CLI source or package before installation, prefer npx or a scoped install when possible, and rotate or revoke API keys from the dLazy dashboard if needed.

Risk: Generation consumes dLazy account credits and can fail when the account has insufficient balance.

Mitigation: Use dry-run cost estimates when appropriate and confirm expected credit usage before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads containing generated image URLs; optional saved image files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation IDs, polling, dry-run cost estimates, and optional local downloads.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
