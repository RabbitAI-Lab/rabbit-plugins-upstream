## Description:

Helps agents find, generate, edit, and reuse image, video, and audio assets in HyperFrames projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to source and produce media for HyperFrames projects, including music, sound effects, imagery, voiceovers, captions, and visual treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running shell tools or unpinned npx hyperframes may execute changed dependencies.

Mitigation: Review the commands and package source before running, and pin tooling where practical.

Risk: Provider setup may install Python model dependencies or launch background processes.

Mitigation: Review installation steps and run them only in an environment where these changes are acceptable.

Risk: Local credential files and reusable media or preferences may be exposed in shared directories.

Mitigation: Review .env and HeyGen authentication behavior; restrict access to ~/.media and avoid sharing credentials.

Risk: PostHog telemetry may be linked to a HeyGen account.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 if telemetry is not acceptable.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Provider setup](references/setup-providers.md)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Media treatments](references/media-treatments.md)
- [HeyGen CLI instructions](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Media files]

**Output Format:** [Markdown guidance, command output, and local media assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets may include a local file path and ledger record.]

## Skill Version(s):

1.0.70 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
