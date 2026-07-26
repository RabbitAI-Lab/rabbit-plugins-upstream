## Description: <br>
End-to-end AI video generation - create videos from text prompts using image generation, video synthesis, voice-over, and editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rhanbourinajd](https://clawhub.ai/user/rhanbourinajd) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to generate short videos from text prompts, assemble image sequences into MP4 files, and add optional narration with cloud AI providers and FFmpeg. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provider API keys or confidential prompts, scripts, images, audio, or videos may be exposed to cloud services. <br>
Mitigation: Keep API keys scoped and private, and avoid sending confidential content unless the providers' data policies are acceptable. <br>
Risk: Paid provider API calls can create unexpected usage costs. <br>
Mitigation: Monitor provider usage and choose budget or free workflow options when cost control is required. <br>
Risk: Local FFmpeg processing and output handling may be affected by unusual filenames or overwrite selected output paths. <br>
Mitigation: Review input filenames and output paths before execution, and keep FFmpeg and Python dependencies updated. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rhanbourinajd/skills/ai-video-gen) <br>
- [OpenAI Platform](https://platform.openai.com) <br>
- [LumaAI](https://lumalabs.ai) <br>
- [Runway](https://runwayml.com) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [Replicate](https://replicate.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell commands, configuration steps, and generated media file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create images, audio, and MP4 files via provider APIs and FFmpeg when commands are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
