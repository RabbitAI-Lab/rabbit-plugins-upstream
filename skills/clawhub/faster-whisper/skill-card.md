## Description: <br>
Local speech-to-text using faster-whisper. 4-6x faster than OpenAI Whisper with identical accuracy; GPU acceleration enables ~20x realtime transcription. SRT/VTT/TTML/CSV subtitles, speaker diarization, URL/YouTube input, batch processing with ETA, transcript search, chapter detection, per-file language map. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theplasmak](https://clawhub.ai/user/theplasmak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe local audio/video, URLs, YouTube media, or podcast feeds into transcripts, subtitles, searchable segments, chapter markers, and optional speaker-labeled output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch user-provided remote media and podcast feeds. <br>
Mitigation: Use trusted URLs or feeds and run remote-media transcription in a constrained workspace. <br>
Risk: The skill can access local media files and persist generated transcript, subtitle, data, or speaker-audio outputs. <br>
Mitigation: Review input and output paths before running, and avoid processing sensitive media unless file retention is acceptable. <br>
Risk: The --update path can persistently change the skill's runtime dependency. <br>
Mitigation: Avoid --update in normal runs and update dependencies through a controlled package-management process. <br>
Risk: Optional diarization and private model workflows can use HuggingFace credentials. <br>
Mitigation: Prefer cached credentials where appropriate and avoid passing tokens directly in reusable command history. <br>


## Reference(s): <br>
- [Faster Whisper ClawHub Release](https://clawhub.ai/theplasmak/skills/faster-whisper) <br>
- [Faster Whisper Source Homepage](https://github.com/ThePlasmak/faster-whisper) <br>
- [SYSTRAN faster-whisper](https://github.com/SYSTRAN/faster-whisper) <br>
- [Distil-Whisper Paper](https://arxiv.org/abs/2311.00430) <br>
- [SYSTRAN faster-whisper Hugging Face Models](https://huggingface.co/collections/Systran/faster-whisper) <br>
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) <br>
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated transcript, subtitle, JSON, CSV, TSV, HTML, TTML, ASS, LRC, and speaker-audio files when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may be written to stdout or filesystem paths depending on requested format and -o usage; batch and multi-format runs can produce multiple files.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
