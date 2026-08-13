## Description:

Generate and edit video with Veo 3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and agents use this skill to create, edit, or transform video with Veo 3 through RunAPI. For one-off generation it guides use of the RunAPI CLI; for application integration it directs developers to the current SDK references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill can authenticate to RunAPI, submit video-generation tasks, upload local media included in requests, and download generated media.

Mitigation: Confirm RunAPI account, billing, credential handling, and media upload intent before installation or use.

Risk: Interactive browser login and background task execution can change user expectations about authorization or completion status.

Mitigation: Use environment or approved CLI authentication by default, and use browser login or background execution only when explicitly requested.

Risk: Generated media may be missing, empty, or returned with an unexpected content type.

Mitigation: Download every requested deliverable and verify both non-empty file contents and expected MIME type before reporting completion.

## Reference(s):

- [RunAPI Veo 3.1 model homepage](https://runapi.ai/models/veo-3.1)
- [RunAPI Veo 3.1 model documentation](https://runapi.ai/models/veo-3.1.md)
- [RunAPI Google provider overview](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Veo 3.1 SDK integration](https://github.com/runapi-ai/veo-3.1-sdk)
- [RunAPI Veo 3.1 variant](https://runapi.ai/models/veo-3.1/veo-3.1.md)
- [RunAPI Veo 3.1 Fast variant](https://runapi.ai/models/veo-3.1/fast.md)
- [RunAPI Veo 3.1 Lite variant](https://runapi.ai/models/veo-3.1/lite.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown with shell commands, JSON request files, SDK guidance, and downloaded media file verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for authenticated RunAPI video-generation workflows; media deliverables are external service outputs that must be downloaded and MIME-checked.]

## Skill Version(s):

0.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
