## Description: <br>
Generate images using a local ComfyUI instance with a configured local/private server address and allowlisted workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hypnotronic3](https://clawhub.ai/user/hypnotronic3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to ask an agent to generate images through a trusted local or private ComfyUI deployment. It supports prompt, negative prompt, workflow, dimension, seed, and timeout controls while restricting workflows to the bundled allowlist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generated images may be sensitive and are written to disk. <br>
Mitigation: Use only trusted local or private ComfyUI servers, and review or clean both the skill output folder and the ComfyUI output folder after sensitive work. <br>
Risk: Bundled workflows may require specific ComfyUI custom nodes, model files, and significant GPU or CPU resources. <br>
Mitigation: Confirm the local ComfyUI environment has the required nodes, models, and available compute before running the skill. <br>
Risk: Using an untrusted ComfyUI endpoint could expose prompts or generated outputs to another system. <br>
Mitigation: Set COMFYUI_SERVER_ADDRESS only to a trusted localhost, private IP, or local network host. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hypnotronic3/skills/comfyui-local) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/hypnotronic3) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files, guidance] <br>
**Output Format:** [Console text with MEDIA file path lines for generated images] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated images to the skill output folder after polling the configured ComfyUI server.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
