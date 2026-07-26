## Description: <br>
Edge TTS converts text into speech audio with configurable voices, languages, speed, pitch, volume, and optional subtitle generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[i3130002](https://clawhub.ai/user/i3130002) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to convert requested text, summaries, or messages into speech audio for accessibility, multitasking, or voice delivery. It supports choosing voices, languages, prosody settings, output quality, and optional subtitle timing data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for conversion is sent to Microsoft's online TTS service, which can expose sensitive content outside the local environment. <br>
Mitigation: Do not use the skill for secrets, regulated data, private documents, or confidential prompts. <br>
Risk: Generated audio files can remain in the temporary output directory and may contain sensitive spoken content. <br>
Mitigation: Periodically clean generated audio files from the temporary directory or direct outputs to a managed location with appropriate retention controls. <br>


## Reference(s): <br>
- [node-edge-tts Reference](references/node_edge_tts_guide.md) <br>
- [Voice Testing](https://tts.travisvn.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [MP3 audio files, optional JSON subtitles, and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires internet access to Microsoft's online TTS service; generated audio files may be written to a temporary directory until cleaned up.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata, skill-info.json, scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
