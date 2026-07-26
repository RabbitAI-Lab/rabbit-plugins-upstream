## Description: <br>
Novel2Voice helps an agent convert novel text or SRT/ASS subtitle files into multi-character narrated audiobook or dubbing audio using Edge TTS by default and optional MiMo TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jangviktor-web](https://clawhub.ai/user/jangviktor-web) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to turn pasted story text, novel files, or video subtitle files into narrated multi-role audio. It guides role detection, voice assignment, TTS backend selection, confirmation, and execution of local scripts that generate audio and logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Novel or subtitle content may be sent to configured remote TTS services. <br>
Mitigation: Use only with text that can be shared with the selected endpoint, and avoid private manuscripts or confidential subtitles unless the endpoint is trusted. <br>
Risk: TTS API keys may be read from environment variables, a skill-local .env file, or ~/.openclaw/openclaw.json, and the skill may persist keys locally. <br>
Mitigation: Prefer environment variables or a managed secret store, avoid pasting keys into chat, and review or remove skill-local .env files after use. <br>
Risk: Generated output directories and caches can contain audio, copied segments, subtitles, and logs derived from user content. <br>
Mitigation: Store outputs in an appropriate directory, review generated files before sharing, and delete local output or cache files when the source content is sensitive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jangviktor-web/skills/novel2voice) <br>
- [Server-Resolved GitHub Source](https://github.com/jangviktor-web/novel2voice-clawskill) <br>
- [Voice Catalog](references/voice-catalog.md) <br>
- [MiMo TTS API Reference](references/mimo-tts-api.md) <br>
- [Edge TTS Annotation Guide](references/edge-tts-annotation-guide.md) <br>
- [Long Text Handling Details](references/generated-long-body.md) <br>
- [MiMo TTS Console](https://mimo.xiaomi.com) <br>
- [Microsoft Edge TTS Reference Link](https://edge.microsoft.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with tables and bash commands; generated artifacts include WAV/MP3 audio, subtitle files, JSON logs, and segment files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill normally writes outputs under a user-selected output directory and may create local configuration or cache files for TTS backends.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 2.19.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
