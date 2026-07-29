## Description: <br>
Generates and edits AI music through RunComfy by routing requests to ElevenLabs Music or ACE Step models and producing the matching runcomfy CLI invocation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to generate songs, background music, jingles, multilingual vocal tracks, or edits to existing audio through RunComfy model endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy generation can use an API token and incur per-generation cloud costs. <br>
Mitigation: Confirm the user's intent before running generation, keep RUNCOMFY_TOKEN out of prompts and logs, and review the selected model cost before long or batch jobs. <br>
Risk: Music prompts, lyrics, and source audio URLs may involve content the user does not have rights to use. <br>
Mitigation: Use only user-provided or authorized lyrics and audio URLs, and ask the user to confirm rights before generating around supplied copyrighted material. <br>
Risk: Editing workflows depend on external audio URLs and generated output may not match the requested style or section boundaries. <br>
Mitigation: Use only URLs supplied for the task, inspect generated audio before relying on it, and rerun or adjust route parameters when the output diverges from the prompt. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/ai-music-runcomfy) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>
- [RunComfy audio models catalog](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>
- [ElevenLabs Music model page](https://www.runcomfy.com/models/elevenlabs/elevenlabs/music-generation?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>
- [ACE Step text-to-audio model page](https://www.runcomfy.com/models/acestep-ai/ace-step/text-to-audio?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>
- [ACE Step audio-inpaint model page](https://www.runcomfy.com/models/acestep-ai/ace-step/audio-inpaint?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>
- [ACE Step audio-outpaint model page](https://www.runcomfy.com/models/acestep-ai/ace-step/audio-outpaint?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-music-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON CLI inputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model-route selection guidance, RunComfy CLI invocations, authentication requirements, and output-directory instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
