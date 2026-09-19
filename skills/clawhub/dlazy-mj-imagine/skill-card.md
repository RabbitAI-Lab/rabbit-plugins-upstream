## Description:

Generates Midjourney-style images through the dLazy CLI, with controls for aspect ratio, bot type, and grid or upscaled output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create artistic, strongly stylized images through dLazy's hosted image-generation service. It is suited for prompt-driven creative image generation where the user wants CLI-level control over aspect ratio, Midjourney or Niji bot type, and output slot selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and any referenced local media may be sent to the dLazy hosted service.

Mitigation: Review prompts and file paths before use, and avoid sending sensitive content unless the user has approved the dLazy service for that data.

Risk: Using dLazy authentication stores an API key in local CLI configuration unless the key is supplied per invocation.

Mitigation: Prefer per-invocation environment variables where persistence is not desired, and rotate or revoke dLazy API keys when access should change.

Risk: Generated files may be written locally when the CLI is run with a save path.

Mitigation: Use --save only with paths where generated assets are intended to be written.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI can return hosted image URLs, asynchronous task IDs, and optionally save generated assets to a user-specified local path.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
