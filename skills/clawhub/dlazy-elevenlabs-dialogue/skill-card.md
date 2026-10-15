## Description:

Generates multi-voice dialogue audio from scripted lines using ElevenLabs eleven_v3 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn character dialogue, podcast scripts, and short skits into multi-voice audio with optional emotional delivery cues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to dLazy's hosted service.

Mitigation: Review content before submission and avoid including sensitive material without authorization.

Risk: The CLI may store a dLazy API key locally.

Mitigation: Review the pinned CLI package before installing and use DLAZY_API_KEY per invocation if local key storage is unsuitable.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can return an asset URL or save a generated file; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
