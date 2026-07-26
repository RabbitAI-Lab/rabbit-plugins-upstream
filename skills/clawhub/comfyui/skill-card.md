## Description: <br>
Run local ComfyUI workflows via the HTTP API. Use when the user asks to run ComfyUI, execute a workflow by file path/name, or supply raw API-format JSON; supports the default workflow bundled in assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kelvincai522](https://clawhub.ai/user/kelvincai522) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and image-generation users use this skill to run local ComfyUI workflows, edit workflow JSON for prompts, styles, and seeds, download model weights, and return generated images from a local ComfyUI server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install and run an unpinned pget helper program when pget is not already available. <br>
Mitigation: Prefer --no-pget or install pget from a verified source before using the download helper. <br>
Risk: The skill can persist arbitrary model downloads into the local ComfyUI models directory. <br>
Mitigation: Download model files only from trusted sources, verify hashes when available, and avoid --overwrite for untrusted files. <br>
Risk: Workflow JSON controls the local ComfyUI job that will be queued. <br>
Mitigation: Review workflow JSON before running it, especially when supplied by another user or source. <br>


## Reference(s): <br>
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI.git) <br>
- [pget](https://github.com/replicate/pget) <br>
- [ClawHub Skill Page](https://clawhub.ai/kelvincai522/skills/comfyui) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-producing helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The run helper prints JSON containing a prompt_id and generated image metadata; model downloads persist files under the local ComfyUI models directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
