## Description:

Guides agents to create fast lip-synced video from video and audio through the dLazy HeyGen Lipsync Speed CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide fast lip-sync generation from a video and audio input with the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy's hosted service, and authentication requires a dLazy API key.

Mitigation: Use only approved media and a protected API key; confirm that dLazy's hosted service is acceptable before use.

Risk: The skill documentation conflicts on required arguments and output type.

Mitigation: Check `dlazy heygen-lipsync-speed -h` and confirm the actual result before relying on an output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reports JSON results with hosted asset URLs or an asynchronous task ID; it can optionally save an asset locally.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; skill frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
