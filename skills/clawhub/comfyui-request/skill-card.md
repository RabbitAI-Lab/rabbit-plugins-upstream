## Description: <br>
Send a workflow request to ComfyUI and return image results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtopher86](https://clawhub.ai/user/xtopher86) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to submit ComfyUI workflows to a configured ComfyUI server and retrieve generated image results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workflows, prompts, and generated image metadata are sent to the configured ComfyUI server. <br>
Mitigation: Use only a ComfyUI server you control or trust, and set COMFYUI_HOST and COMFYUI_PORT deliberately. <br>
Risk: Optional basic authentication credentials may be sent to the ComfyUI server. <br>
Mitigation: Avoid reusing important passwords for COMFYUI_USER and COMFYUI_PASS, and prefer localhost, a trusted LAN or VPN, or an HTTPS reverse proxy when prompts or credentials are sensitive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xtopher86/skills/comfyui-request) <br>
- [Publisher Profile](https://clawhub.ai/user/xtopher86) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON response containing status, prompt identifiers, image metadata, and image URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a reachable ComfyUI server; supports optional basic authentication and configurable timeout and polling intervals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
