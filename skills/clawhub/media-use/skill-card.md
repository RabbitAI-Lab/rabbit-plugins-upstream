## Description:

Helps HyperFrames users find, generate, edit, and reuse media, including music, effects, images, voiceovers, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators use this skill to source or generate project media, produce voiceovers and captions, edit footage, and reuse assets in HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External media providers may receive requests and use locally stored credentials.

Mitigation: Review provider access and avoid running in workspaces with unrelated secrets in parent .env files.

Risk: Untrusted audio_request.json line IDs can cause writes outside the intended project.

Mitigation: Treat audio requests from untrusted projects as unsafe until line IDs are validated.

Risk: The skill writes project and global media caches and sends opt-out usage telemetry.

Mitigation: Review local write locations and set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 to disable telemetry.

Risk: Running an unpinned hyperframes version may change the code executed by media commands.

Mitigation: Prefer a pinned or plugin version of hyperframes.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Audio workflows](artifact/references/audio.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Provider setup](artifact/references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI output with paths to saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save media assets and project ledger records locally.]

## Skill Version(s):

1.0.71 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
