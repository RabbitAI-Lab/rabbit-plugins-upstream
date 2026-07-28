## Description: <br>
Relight still images by changing lighting setup, color temperature, direction, or mood through RunComfy's `runcomfy` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and image-production agents use this skill to route still-image relighting requests to RunComfy models and produce the right CLI invocation for the desired lighting change. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends still images or image URLs to RunComfy for relighting. <br>
Mitigation: Use it only when the user intends to send the image to RunComfy, and pass only images or URLs the user explicitly provided for the relight task. <br>
Risk: RunComfy authentication tokens may be exposed if copied into prompts, logs, or shared shell history. <br>
Mitigation: Keep `RUNCOMFY_TOKEN` in the environment or RunComfy's protected config and avoid echoing token values in agent output. <br>
Risk: A broad lighting-related request may be interpreted as permission to edit an image. <br>
Mitigation: Confirm intent before invoking the skill when the user mentions lighting but does not clearly ask to relight or edit a still image. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/relight) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=relight) <br>
- [Qwen Edit Relight model](https://www.runcomfy.com/models/qwen/qwen-edit-2509/lora/relight?utm_source=clawhub&utm_medium=skill&utm_campaign=relight) <br>
- [RunComfy Qwen Image collection](https://www.runcomfy.com/models/collections/qwen-image?utm_source=clawhub&utm_medium=skill&utm_campaign=relight) <br>
- [RunComfy image editing models collection](https://www.runcomfy.com/models/collections/best-image-editing-models?utm_source=clawhub&utm_medium=skill&utm_campaign=relight) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the `runcomfy` CLI, requires `RUNCOMFY_TOKEN` or RunComfy login, and writes generated image results to the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
