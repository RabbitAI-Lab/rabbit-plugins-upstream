## Description:

Use when someone wants a person on camera speaking a script - lip-synced host, spokesperson, or narrated avatar from a portrait photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to prepare a single Pruna p-video-avatar prediction that turns an approved portrait and script or narration audio into a lip-synced talking-head avatar clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected portraits, scripts, and optional narration audio to Pruna's API.

Mitigation: Confirm each media asset before generation, avoid uploading unnecessary optional files, and use a dedicated API key with normal account controls.

Risk: Generated avatar output can drift from the approved speaker, script, or delivery intent.

Mitigation: Review the video prompt, voice fields, resolution, and source media with the user before any paid API call.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-avatar)
- [Pruna files API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with curl commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one p-video-avatar prediction workflow per invocation; async creation is recommended, with sync reserved for quick tests.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
