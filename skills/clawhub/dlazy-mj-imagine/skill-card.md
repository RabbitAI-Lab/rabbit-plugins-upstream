## Description:

Helps agents generate stylized images with dLazy's Midjourney-style service, with aspect-ratio, bot, and grid or upscale selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized images with a chosen aspect ratio and select a grid or upscale result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation settings, and media files explicitly supplied as inputs are sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive content unless you are comfortable sharing it with dLazy.

Risk: Using the skill requires a dLazy API key saved by the CLI or supplied for the session.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard if needed.

Risk: Installing the pinned third-party npm CLI executes external software.

Mitigation: Review the CLI before installing; use the pinned npx form if a persistent global installation is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted image URLs or an asynchronous task ID; the --save option downloads a result.]

## Skill Version(s):

1.3.26 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
