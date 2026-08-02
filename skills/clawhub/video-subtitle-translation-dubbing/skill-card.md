## Description: <br>
Multi-language video subtitle translation and automatic dubbing skill (supports English, Chinese, Japanese, Spanish, French, German, Korean, etc.). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbjincheng](https://clawhub.ai/user/zbjincheng) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agents use this skill to translate video subtitles across languages and optionally synthesize target-language dubbing. It produces a translated subtitle file and a muxed video with target-language subtitles and, when enabled, target-language audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subtitle text, transcript-derived content, and provider credentials can be sent to the translation or TTS endpoints configured by the user. <br>
Mitigation: Use only trusted endpoints, avoid sensitive or restricted media unless approved, and review temporary and output files after runs. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/zbjincheng/openclaw-skill-videotranslate) <br>
- [ClawHub skill page](https://clawhub.ai/zbjincheng/skills/video-subtitle-translation-dubbing) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Media] <br>
**Output Format:** [JSON-like result containing output_video_path and output_subtitle_path for generated MKV and UTF-8 SRT/VTT files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured translation and, for dubbing mode, TTS providers; reports progress through parsing, translating, optional TTS, muxing, and done stages.] <br>

## Skill Version(s): <br>
0.1.3 (source: frontmatter and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
