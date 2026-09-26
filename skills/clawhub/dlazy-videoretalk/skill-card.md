## Description:

视频对口型 Video Retalk helps agents run dLazy's Tongyi VideoRetalk service to generate a talking-person video whose mouth movements match a supplied speech audio track, with an optional reference face image for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content-production agents use this skill to invoke dLazy VideoRetalk for lip sync, dubbing, and mouth synchronization workflows that combine an input talking-person video with a replacement voice track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and hosted API, so API keys may be stored locally and video, audio, or reference image inputs may be uploaded for processing.

Mitigation: Review dLazy account, key storage, and data-handling requirements before use; rotate or revoke API keys from the dLazy dashboard when needed.

Risk: The inspected examples contain parameter mistakes according to the security guidance.

Mitigation: Use `dlazy videoretalk -h` as the authoritative source for current flags and required parameters before running a job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated-media URLs, asynchronous task identifiers, or saved local output files when the CLI save option is used.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
