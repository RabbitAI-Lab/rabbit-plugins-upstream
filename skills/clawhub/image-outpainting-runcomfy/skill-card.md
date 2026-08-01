## Description: <br>
Image outpainting on RunComfy via the runcomfy CLI extends still images beyond their original canvas, changes aspect ratio, and routes requests across RunComfy image-edit endpoints based on the outpainting scenario. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-production users use this skill to extend existing still images, uncrop photos, and change aspect ratios through RunComfy-hosted image-edit models from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends selected prompts and image URLs to RunComfy-hosted services. <br>
Mitigation: Use only prompts and image URLs the user intended to provide for the edit, and confirm comfort with RunComfy processing before running the CLI. <br>
Risk: The skill requires a RunComfy API token stored locally or supplied through RUNCOMFY_TOKEN. <br>
Mitigation: Store the token through runcomfy login or a controlled environment variable, and avoid exposing it in prompts, logs, or shared shell history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/image-outpainting-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI docs](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=image-outpainting-runcomfy) <br>
- [Best image editing models](https://www.runcomfy.com/models/collections/best-image-editing-models?utm_source=clawhub&utm_medium=skill&utm_campaign=image-outpainting-runcomfy) <br>
- [Nano Banana 2 Edit](https://www.runcomfy.com/models/google/nano-banana-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=image-outpainting-runcomfy) <br>
- [RunComfy ComfyUI workflows](https://www.runcomfy.com/comfyui-workflows?utm_source=clawhub&utm_medium=skill&utm_campaign=image-outpainting-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI, RUNCOMFY_TOKEN or local RunComfy login, and RunComfy configuration under ~/.config/runcomfy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
