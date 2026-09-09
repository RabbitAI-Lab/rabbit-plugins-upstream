## Description:

Agent Media OS for HyperFrames projects that resolves, generates, operates on, and reuses media assets including BGM, SFX, images, icons, logos, voices, color grades, LUTs, captions, transcription, and background removal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to find, generate, transform, and reuse media assets while building HyperFrames projects. It helps agents turn media intent into local assets, paste-ready blocks, ledger records, or operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-linked telemetry may be undesirable in sensitive environments.

Mitigation: Disable telemetry with DO_NOT_TRACK=1 or HYPERFRAMES_NO_TELEMETRY=1 before use.

Risk: Cross-project media storage can retain assets beyond a single project boundary.

Mitigation: Inspect and periodically clear ~/.media, especially between clients or confidential projects.

Risk: Remote media ingestion can bring untrusted content into a project.

Mitigation: Avoid --from with untrusted URLs and prefer vetted local files or known providers.

Risk: Optional package or model installs can change the local execution environment.

Mitigation: Run optional installs inside an isolated environment and use --local-only for confidential media workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Setup and providers](references/setup-providers.md)
- [Resolve reference](references/resolve.md)
- [Media treatments](references/media-treatments.md)
- [Operations reference](references/operations.md)
- [Audio reference](references/audio.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [Pixabay sound effects](https://pixabay.com/sound-effects/)
- [Pixabay Content License summary](https://pixabay.com/service/license-summary/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, paste-ready blocks, and local media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reference local media files, manifests, cache entries, captions, transcripts, cut lists, treatment payloads, and LUT files.]

## Skill Version(s):

1.0.45 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
