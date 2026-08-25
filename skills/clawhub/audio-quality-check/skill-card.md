## Description:

Analyzes audio recording quality, including echo detection, loudness, speech intelligibility, SNR, and spectral analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, audio engineers, and support teams use this skill to inspect call recordings, compare original and processed tracks, and diagnose issues such as echo, low intelligibility, noise, or abnormal loudness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private extracted audio can remain in temporary files when some analysis modes exit before cleanup.

Mitigation: Avoid shortcut modes for sensitive recordings, or manually delete /tmp/audio_analysis_* and related extracted WAV files after analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/audio-quality-check)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/audio-quality-check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and terminal analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports track metadata, loudness, echo correlation, speech quality, intelligibility, spectral metrics, SNR, and per-minute energy when supported by the recording inputs.]

## Skill Version(s):

0.1.4 (source: SKILL.md frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
