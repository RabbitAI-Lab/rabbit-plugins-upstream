## Description:

Video Retalk regenerates a talking-person video so the speaker's lip movements match a supplied voice audio track, with an optional reference face image for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted VideoRetalk service for lip-syncing a person video to a new speech audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected video, audio, and optional face image inputs to dLazy-hosted services.

Mitigation: Use media you are authorized to upload and avoid sensitive personal media unless the dLazy service terms and your workflow requirements permit it.

Risk: The skill requires a dLazy API key and may store it in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or the npx path when you do not want a persistent global binary or saved local key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs; asynchronous runs may return a generateId for polling.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
