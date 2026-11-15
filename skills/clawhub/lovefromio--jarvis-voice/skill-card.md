## Description:

Turn your AI into JARVIS. Voice, wit, and personality — the complete package. Humor cranked to maximum.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovefromio](https://clawhub.ai/user/lovefromio)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users can use the skill to render opted-in English replies as local JARVIS-style speech and provide matching chat text. Developers can optionally apply its session, voice, and humor templates to shape agent responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Spoken replies can be overheard, and the server security guidance notes that the skill uses shell commands and may delete local voice, session, and humor configuration files.

Mitigation: Keep speech opt-in, mute it when needed, avoid speaking sensitive content, and review the optional template removal command before using it.

Risk: The scanner evidence is incomplete because three local path-like references were unresolved.

Mitigation: Review the shipped script and referenced local files before installation, especially if changing the package or its dependencies.

## Reference(s):

- [Jarvis Voice on ClawHub](https://clawhub.ai/lovefromio/skills/jarvis-voice)
- [TinkerClaw project](https://github.com/globalcaos/tinkerclaw)
- [LIMBIC computational humor research](https://thetinkerzone.com/humor-embeddings-laughter-from-inverted-memory-bisociation-in-computational-embedding-space/)
- [sherpa-onnx Piper Alan model download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-alan-medium.tar.bz2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio, Configuration guidance, Shell commands]

**Output Format:** [Markdown replies, local spoken audio, and optional prompt-template instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English-only speech using the bundled Alan voice; audio playback is local, and the three behavior templates are optional.]

## Skill Version(s):

3.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
