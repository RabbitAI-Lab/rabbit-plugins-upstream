## Description: <br>
Helps agents generate light instrumental background music with Stable Audio 2.5 on Replicate, such as ambient beds under dialogue or underscores for reels and explainers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to prompt Stable Audio 2.5 for short instrumental background beds, confirm required inputs and credentials, submit a Replicate prediction, poll for completion, and download the generated MP3. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on additional PrunaAI skills that can expand what is installed or loaded for the agent. <br>
Mitigation: Review the referenced dependency skills before installing or using this skill. <br>
Risk: Prompts and generated audio are sent through Replicate when the API request is made. <br>
Mitigation: Use the skill only when that data flow is acceptable for the content being generated. <br>
Risk: A Replicate API token is required for generation. <br>
Mitigation: Keep the token in the environment and do not hardcode it in files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5) <br>
- [Replicate Stable Audio 2.5 prediction endpoint](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Replicate API token for generation and ffmpeg/ffprobe for the mix step.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
