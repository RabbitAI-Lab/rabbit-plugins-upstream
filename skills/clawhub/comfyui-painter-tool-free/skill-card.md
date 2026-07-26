## Description: <br>
A local ComfyUI text-to-image guide for basic workflows, default model setup, parameter tuning, and saving generated images for personal creative use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run local ComfyUI text-to-image workflows, tune common generation parameters, and save generated images without a cloud API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Starting ComfyUI on 0.0.0.0 can expose the service to the wider network without access-control guidance. <br>
Mitigation: Bind ComfyUI to 127.0.0.1 unless remote LAN access is intentional and protected with firewall or authentication controls. <br>
Risk: The skill asks the agent to run local shell commands and download ComfyUI, Python dependencies, and model files. <br>
Mitigation: Review commands before execution and install dependencies only from trusted sources in an isolated environment when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/comfyui-painter-tool-free) <br>
- [Stable Diffusion v1.5 checkpoint](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, files] <br>
**Output Format:** [Markdown guidance with shell and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local image files through ComfyUI; no cloud API key is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
