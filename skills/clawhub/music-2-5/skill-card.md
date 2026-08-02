## Description: <br>
Use this skill when someone wants an original AI song with vocals, sung lyrics, a style prompt track, or source audio for a music video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, developers, and agents use this skill to generate original vocal songs through Replicate/MiniMax from lyrics, style prompts, and audio settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lyrics, style prompts, and generated-audio requests are sent to Replicate and MiniMax. <br>
Mitigation: Confirm the user is comfortable sending this content to those services before generating. <br>
Risk: The workflow requires a Replicate API token and points agents to related Pruna skills. <br>
Mitigation: Verify REPLICATE_API_TOKEN handling and review the related Pruna skills before using them in the workspace. <br>


## Reference(s): <br>
- [music-2.5 on ClawHub](https://clawhub.ai/pruna-ai/skills/music-2-5) <br>
- [MiniMax privacy policy](https://www.minimax.io/platform/protocol/privacy-policy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl examples and environment variable configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN and may reference ffmpeg/ffprobe for follow-on music-video assembly.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
