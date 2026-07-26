## Description: <br>
Use when crafting TTS, music, or bed prompts for any generative audio model - director style, song structure, and post-production layering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to draft speech, music, and background-bed prompts, choose the right audio generation path, and plan narration-plus-music layering for video or audio production. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to install related Pruna skills or use paid audio and video APIs. <br>
Mitigation: Review suggested related-skill installs before accepting them and confirm before paid generation, uploads, or API calls. <br>
Risk: Audio and video workflows may require credentials such as PRUNA_API_KEY or REPLICATE_API_TOKEN. <br>
Mitigation: Keep API keys in the intended environment variables and avoid placing secrets in prompts, generated files, or shared logs. <br>
Risk: Narration can be truncated when audio is longer than the target video model's clip limit. <br>
Mitigation: Probe generated audio duration, keep per-scene lines within the documented limit, and split long narration into multiple scene rows. <br>


## Reference(s): <br>
- [TTS style prompting](references/tts-style-prompting.md) <br>
- [Music and bed prompting](references/music-and-bed-prompting.md) <br>
- [Audio post-production](references/audio-post-production.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with prompt examples, workflow steps, command snippets, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May suggest related skill installs, API-key environment variables, audio duration checks, and ffmpeg-based assembly steps when the task requires them.] <br>

## Skill Version(s): <br>
1.0.7 (source: server evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
