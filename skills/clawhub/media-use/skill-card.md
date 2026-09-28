## Description:

Helps agents find, generate, edit, and reuse media for HyperFrames projects, including audio, images, video, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers working on HyperFrames projects use this skill to source and produce media, make audio and visual edits, and prepare reusable assets for their compositions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage telemetry may be linked to a HeyGen account by default.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 before use if account-linked telemetry is unwanted.

Risk: Provider workflows access local credentials and may send requests to external services.

Mitigation: Review project .env files and provider access before running; use local-only options when external calls are not appropriate.

Risk: Unpinned npx hyperframes commands may execute a changing CLI version.

Mitigation: Prefer a pinned or locally installed CLI version when possible.

## Reference(s):

- [Media Use on ClawHub](https://clawhub.ai/heygen-com/skills/media-use)
- [Provider setup](references/setup-providers.md)
- [Telemetry and privacy](references/meta.md)
- [HeyGen CLI setup](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with shell commands, file paths, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May identify locally saved media assets and reusable recipes.]

## Skill Version(s):

1.0.61 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
