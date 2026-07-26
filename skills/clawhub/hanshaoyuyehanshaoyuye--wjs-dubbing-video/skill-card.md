## Description: <br>
Generates TTS dubbing audio from translated SRT subtitles using Edge-TTS and outputs a single MP3 dub track for video synthesis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hanshaoyuyehanshaoyuye](https://clawhub.ai/user/hanshaoyuyehanshaoyuye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video localization workflows use this skill to turn translated SRT subtitles into timeline-aligned dubbing audio. It provides commands for Chinese, English, and voice-specific TTS generation and for use in a larger subtitle-burning pipeline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subtitle text may be sent to Edge-TTS when users run the referenced dubbing workflow. <br>
Mitigation: Use only subtitle content approved for that service and avoid sending private or sensitive text unless the service use is acceptable. <br>
Risk: The skill references companion scripts that are not bundled in the artifact. <br>
Mitigation: Run companion scripts only from a trusted source and review them before execution. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for creating a single MP3 dub track aligned to SRT subtitle timing.] <br>

## Skill Version(s): <br>
8.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
