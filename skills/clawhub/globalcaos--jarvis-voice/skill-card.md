## Description:

Adds a JARVIS-style local voice and persona guidance to an OpenClaw agent, including optional dry-wit templates and offline text-to-speech playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to add local spoken responses, a visible Jarvis-style Markdown line, and optional persona templates to interactive home-chat sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audio playback can disclose spoken content to people nearby.

Mitigation: Use the documented mute controls, keep sensitive content out of spoken lines, and rely on the channel gates for messaging, cron, and subagent contexts.

Risk: Optional workspace templates can persist persona and session behavior across future sessions.

Mitigation: Prefer per-session use, copy only the specific templates wanted, and remove persistent templates with the documented uninstall command.

Risk: The model download is an unpinned external supply-chain dependency.

Mitigation: Review and verify the downloaded model package before enabling it in controlled or commercial environments.

Risk: The skill installs and runs a local shell command for text-to-speech playback.

Mitigation: Review bin/jarvis before placing it on PATH and confirm the required local dependencies are expected on the target machine.

## Reference(s):

- [TinkerClaw Jarvis Voice release](https://clawhub.ai/globalcaos/skills/jarvis-voice)
- [Piper en_GB Alan voice model download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-alan-medium.tar.bz2)
- [LIMBIC computational humor article](https://thetinkerzone.com/humor-embeddings-laughter-from-inverted-memory-bisociation-in-computational-embedding-space/)
- [Computational Humor related skill](https://clawhub.ai/globalcaos/computational-humor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional template files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English-only voice output; optional local audio playback through bin/jarvis; short spoken lines are recommended.]

## Skill Version(s):

3.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
