## Description:

Synchronizes a speaker's lips in a video to a supplied voice track, with an optional face reference when multiple people appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a talking-person video with a new voice recording, optionally selecting a face in a multi-person video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, audio, and optional face images may be uploaded to dLazy's hosted service.

Mitigation: Review the service terms and submit only media you are comfortable uploading.

Risk: Authentication may save an API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY if you prefer not to store a key on disk.

Risk: The included command and output examples appear inconsistent with this video tool.

Mitigation: Check the CLI help and verify parameters and returned media before relying on examples.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video]

**Output Format:** [JSON response with a generated media URL; optional downloaded video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before media is ready.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
