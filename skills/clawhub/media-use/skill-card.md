## Description:

Helps agents resolve, generate, edit, and reuse media for HyperFrames projects, including audio, images, video treatments, and captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find or generate project media, produce voiceover and captions, edit footage, and reuse assets across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted audio requests may cause generated audio to be written outside the project.

Mitigation: Process only trusted projects and avoid untrusted audio_request.json files until line IDs are sanitized.

Risk: Unpinned runtime tools may execute code that has not been reviewed.

Mitigation: Review the skill before installation and prefer pinned or locked HyperFrames commands.

Risk: Media may be sent to configured third-party providers.

Mitigation: Review provider settings and credentials before sending sensitive media to HeyGen, Gemini, ElevenLabs, or other configured tools.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Audio workflows](artifact/references/audio.md)
- [Media operations](artifact/references/operations.md)
- [Provider setup](artifact/references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, Configuration instructions]

**Output Format:** [Text and Markdown guidance with commands and paths to generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets can be recorded in a project ledger for reuse.]

## Skill Version(s):

1.0.72 (source: ClawHub release record)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
