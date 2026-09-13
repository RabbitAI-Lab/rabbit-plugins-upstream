## Description:

Adds readable or cinematic captions to an existing single-subject talking-head video while preserving the source footage, using local transcription, subject matting, style selection, preview QA, and final video rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to add subtitles, embedded caption moments, or VFX-style caption treatments to eligible talking-head clips without changing the underlying footage. It is intended for single-subject videos that pass the skill's clip, speech, transcript, and preview-quality gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can update globally installed skills before use.

Mitigation: Confirm the update step with the operator, run in a restricted project environment, and review or pin the updater path before processing user footage.

Risk: Runtime dependencies or remote browser scripts may be fetched during a workflow presented as local.

Mitigation: Pre-provision required model and runtime assets, pin dependency sources, and block remote script loads when handling sensitive videos.

Risk: Incorrect transcription, poor matting, or unsuitable source footage can produce misleading or unreadable captions.

Mitigation: Apply the skill's clip refusal gates, sanity-check transcripts, and review preview frames before rendering final video.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [CATALOG.md](CATALOG.md)
- [Rail track](references/rail.md)
- [Composition craft](references/composition-craft.md)
- [DNA registry](dna/README.md)
- [Theme mode](themes/README.md)
- [GSAP runtime](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project configuration, preview artifacts, and captioned video outputs through the described local workflow.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
