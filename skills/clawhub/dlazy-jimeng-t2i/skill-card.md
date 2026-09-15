## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate images from text prompts through the dLazy Jimeng text-to-image CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm CLI and the dLazy hosted service.

Mitigation: Prefer the pinned on-demand npx invocation when possible and review the package or source before use.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use OS user-restricted config permissions or per-invocation environment variables, and rotate or revoke the key if compromise is suspected.

Risk: Local files passed as image inputs may be uploaded to dLazy media storage.

Mitigation: Avoid passing private local files unless upload to the dLazy service is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as dLazy-hosted file URLs, with optional local download through the CLI.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
