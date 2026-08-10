## Description: <br>
Use when someone wants an original AI song with vocals - sung lyrics, a style prompt track, or source audio for a music video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent through generating original vocal music with Replicate's MiniMax music-2.5 model, including lyric intake, style prompting, API invocation, polling, and download steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lyrics and style prompts are sent to Replicate/MiniMax for music generation. <br>
Mitigation: Use the skill only when the user accepts that data sharing, and avoid submitting confidential lyrics, prompts, or source material. <br>
Risk: The workflow requires a Replicate API token and may perform paid API calls. <br>
Mitigation: Confirm REPLICATE_API_TOKEN availability and user intent before making generation requests. <br>
Risk: Follow-on slicing and assembly workflows depend on ffmpeg and ffprobe. <br>
Mitigation: Verify ffmpeg and ffprobe are installed before starting music-video post-processing. <br>


## Reference(s): <br>
- [Replicate MiniMax music-2.5 predictions API](https://api.replicate.com/v1/models/minimax/music-2.5/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides API-token setup, required lyric input, optional generation parameters, prediction polling, output download, and ffmpeg-dependent post-processing workflows.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
