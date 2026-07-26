## Description: <br>
Use when someone wants an original AI song with vocals: sung lyrics, a style prompt track, or source audio for a music video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to prepare Replicate requests for MiniMax music-2.5, collecting lyrics, style prompts, audio format settings, and follow-on workflow guidance for original AI songs with vocals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lyrics and style prompts are sent to Replicate/MiniMax for generation. <br>
Mitigation: Confirm the user is comfortable sharing those inputs with the third-party model provider before making API calls. <br>
Risk: The Replicate API token could be exposed if pasted into prompts, code, or generated files. <br>
Mitigation: Use REPLICATE_API_TOKEN from the environment and avoid echoing or writing the secret value. <br>
Risk: The workflow depends on referenced Pruna helper skills and may require ffmpeg or ffprobe for music-video slicing and assembly. <br>
Mitigation: Install or load the prerequisite skills and confirm required local tools are available before generation or downstream video work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-2-5) <br>
- [Replicate MiniMax music-2.5 predictions endpoint](https://api.replicate.com/v1/models/minimax/music-2.5/predictions) <br>
- [MiniMax privacy policy](https://www.minimax.io/platform/protocol/privacy-policy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API requests] <br>
**Output Format:** [Markdown with inline bash and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to confirm REPLICATE_API_TOKEN, collect lyrics and optional music settings, call Replicate, poll for completion, and download generated audio.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
