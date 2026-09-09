## Description:

Turn your AI into JARVIS. Voice, wit, and personality - the complete package. Humor cranked to maximum.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to add opt-in local JARVIS-style voice playback, visible spoken-line formatting, and optional persona templates to an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local speaker playback can expose spoken responses to nearby people or run in the wrong context.

Mitigation: Use the documented opt-in posture, mute controls, and channel gates before enabling audio playback.

Risk: Optional templates can persistently change future agent behavior if copied into the workspace.

Mitigation: Use templates per session by default and copy only the specific files needed for persistent behavior.

Risk: The model archive is downloaded without an integrity pin.

Mitigation: Review the download source and validate the model artifact through local supply-chain controls before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/jarvis-voice)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [Piper en_GB Alan voice model archive](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-alan-medium.tar.bz2)
- [LIMBIC computational humor article](https://thetinkerzone.com/humor-embeddings-laughter-from-inverted-memory-bisociation-in-computational-embedding-space/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional local audio playback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spoken text should stay short; the included Alan voice model is English-only.]

## Skill Version(s):

3.2.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
