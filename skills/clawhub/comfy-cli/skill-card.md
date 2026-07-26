## Description: <br>
Install, manage, and run ComfyUI instances, including servers, custom nodes, models, workspaces, API workflows, and node-conflict troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johntheyoung](https://clawhub.ai/user/johntheyoung) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and ComfyUI operators use this skill to ask an agent for concise guidance and commands for installing ComfyUI, launching or stopping instances, managing custom nodes and models, running workflows, and troubleshooting broken node setups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ComfyUI install, update, remove, custom-node, and model commands can change a working environment. <br>
Mitigation: Review commands before execution, back up important workflows or snapshots, and install custom nodes and models only from trusted sources. <br>
Risk: Launching ComfyUI with a broad listen address can expose the server beyond the local machine. <br>
Mitigation: Prefer localhost unless remote access is intentional and protected by the user's network controls. <br>
Risk: Model-download workflows may require CivitAI or Hugging Face tokens that could be exposed in commands or logs. <br>
Mitigation: Avoid putting API tokens directly in shared prompts, commands, or logs; use local configuration or secret handling where available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/johntheyoung/skills/comfy-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target a local or selected ComfyUI workspace and may install, update, remove, or run ComfyUI components.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
