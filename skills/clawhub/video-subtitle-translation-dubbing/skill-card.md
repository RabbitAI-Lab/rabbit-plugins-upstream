## Description: <br>
Openclaw Skill Videotranslate translates video subtitles and can generate dubbed audio, producing translated subtitle files and multi-track MKV videos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbjincheng](https://clawhub.ai/user/zbjincheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video localization teams use this skill to translate subtitles and optionally synthesize dubbed audio for input videos when configured with trusted translation and TTS providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video subtitle text and generated audio requests may be sent to configured translation and TTS endpoints. <br>
Mitigation: Use trusted provider URLs, scoped API keys, and provider terms that match the sensitivity of the media being processed. <br>
Risk: The skill reads user-provided video or subtitle paths and writes translated subtitle and MKV output files. <br>
Mitigation: Run it in a controlled workspace and review input paths, output locations, and generated media before sharing or relying on the results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zbjincheng/skills/video-subtitle-translation-dubbing) <br>
- [Server-resolved source repository](https://github.com/zbjincheng/openclaw-skill-videotranslate) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Configuration] <br>
**Output Format:** [Translated subtitle files, multi-track MKV video files, and progress/status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include an output video path and an output subtitle path; dubbing output depends on processing mode and configured providers.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
