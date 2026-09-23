## Description:

Music Toolkit records system playback audio, trims silence or noise, and can split longer music recordings into tracks using AI-assisted structure analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangminrui2022](https://clawhub.ai/user/wangminrui2022)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent record computer playback for a requested duration, save the audio locally, and optionally trim silence or split music recordings into tracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records system playback during the requested window and may capture private, sensitive, or rights-restricted audio.

Mitigation: Use only with explicit recording consent, confirm rights to the source audio, and save outputs to a controlled local directory.

Risk: The skill installs Python packages at runtime and can download FFmpeg automatically, which introduces supply-chain and executable download risk.

Mitigation: Run in an isolated environment, preinstall vetted dependencies from trusted package sources, and verify FFmpeg provenance before use.

Risk: The skill uses a persistent shared virtual environment, so dependency changes may carry across runs.

Mitigation: Use a disposable virtual environment or container for each review or deployment, and reset the environment after execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/music-toolkit)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Text]

**Output Format:** [CLI commands plus local WAV or MP3 audio files and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a duration in minutes; supports optional save directory, filename prefix, silence trimming, AI split mode, silence threshold, and minimum silence length.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
