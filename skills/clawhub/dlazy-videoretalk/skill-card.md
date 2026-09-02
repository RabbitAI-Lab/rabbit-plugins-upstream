## Description:

Tongyi VideoRetalk lip-syncs a talking-person video to a new voice audio track, with an optional reference face image when multiple faces appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external creators use this skill to have an agent call dLazy's hosted VideoRetalk service with a person video and speech audio, producing a video whose mouth movement matches the new audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video, audio, and reference images may be uploaded to dLazy cloud services for processing.

Mitigation: Use only media you have permission to upload, and avoid private, biometric, or non-consensual face, voice, or video material unless approved for this service.

Risk: The skill requires a dLazy API key through local CLI configuration or an environment variable.

Mitigation: Keep API keys out of shared prompts, logs, and repositories; rotate or revoke keys from the dLazy dashboard when access should change.

Risk: Generated output URLs are hosted on dLazy media storage.

Mitigation: Handle returned URLs and downloaded files according to the user's data retention, sharing, and review requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or download generated media with --save; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
