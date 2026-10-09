## Description:

Helps agents create a lip-synced talking-person video from a source video and voice audio, with an optional reference face for multi-person footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a person's mouth movements in a video with new speech audio, optionally selecting a face in multi-person footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, and optional face images may be uploaded to dLazy's hosted service.

Mitigation: Share only media you are authorized to process and review dLazy's service terms before submitting sensitive content.

Risk: Logging in can save a dLazy API key locally, and installing the third-party CLI runs external software.

Mitigation: Protect the saved key and review the CLI before use; prefer the pinned on-demand npx command to avoid a global installation.

Risk: The skill's example command and output sample do not match its documented video and audio inputs.

Mitigation: Check the installed CLI's videoretalk help and validate its actual result before relying on the examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON response]

**Output Format:** [Text guidance and CLI JSON containing a generated-video URL; optional downloaded video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of a completed result.]

## Skill Version(s):

1.3.26 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
