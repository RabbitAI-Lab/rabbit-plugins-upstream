## Description:

Midjourney style generation with controls for aspect ratio, bot type, and output position for artistic and strongly stylized creative image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Midjourney-style images through the dLazy CLI, including selecting aspect ratio, bot type, and grid or upscale output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided media files are sent to dLazy cloud endpoints for generation.

Mitigation: Avoid passing sensitive prompts or files unless the user is comfortable sharing them with dLazy.

Risk: The dLazy API key can be stored in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard if needed.

Risk: The skill depends on network access to dLazy API and media storage endpoints.

Mitigation: Install and run it only in environments where calls to api.dlazy.com and files.dlazy.com are expected and allowed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown with bash commands and JSON or image file results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted image URLs or async task metadata; can save generated PNG assets locally when requested.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
