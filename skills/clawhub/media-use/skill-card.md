## Description:

Helps agents find, generate, edit, and reuse media assets for HyperFrames projects, including audio, imagery, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to source or generate project media, prepare voiceovers and captions, edit footage, and reuse approved assets in HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider requests may use configured cloud credentials and incur charges.

Mitigation: Confirm the selected provider and intended costs before generation; keep unintended keys out of project .env files.

Risk: Telemetry may disclose usage information.

Mitigation: Review telemetry settings and opt out with HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 if needed.

Risk: Local generation may install dependencies or start a background music job.

Mitigation: Confirm local generation before proceeding and review its dependency and job requirements.

Risk: Persistent media caches and changing CLI versions can affect privacy and repeatability.

Mitigation: Review cached assets and use pinned, known-good CLI versions where reproducibility matters.

## Reference(s):

- [Media Use release on ClawHub](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Provider setup](references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Text instructions and commands with local media file paths or paste-ready content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets can be saved locally with ledger records for reuse.]

## Skill Version(s):

1.0.76 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
