## Description:

Helps agents generate short videos from text prompts and optional image, video, audio, or frame references through dLazy's hosted Seedance 2.5 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from prompts, optionally supplying media references or first and last frames, and receive links to generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied image, video, or audio files are sent to dLazy's hosted service.

Mitigation: Review content before submission and avoid sending sensitive media or prompts unless permitted.

Risk: Using the external npm CLI and storing an API key introduces dependency and credential exposure risks.

Mitigation: Review the CLI before installing, use on-demand npx if preferred, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with CLI commands and generated-asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return JSON with hosted asset URLs or an asynchronous task identifier.]

## Skill Version(s):

1.2.22 (source: ClawHub release evidence; CLI install pinned to 1.2.3 in artifact)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
