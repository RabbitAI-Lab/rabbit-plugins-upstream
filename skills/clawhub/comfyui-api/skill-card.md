## Description: <br>
Connects an agent to a ComfyUI server to generate images from prompts, auto-detect server URLs, translate Chinese prompts, and use REST or WebSocket APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qqliaoxin](https://clawhub.ai/user/qqliaoxin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and image-generation users use this skill to connect an agent to a trusted ComfyUI server, submit text-to-image prompts, monitor generation, and retrieve generated image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, workflow data, and uploaded files are sent to the configured ComfyUI server. <br>
Mitigation: Use only a ComfyUI server you control or trust, verify the URL before generation, and avoid sensitive prompts or private files. <br>
Risk: The skill can inspect server history and queue state and can cancel or interrupt work on the configured server. <br>
Mitigation: Install and run it only where the agent is allowed to manage that ComfyUI server's jobs. <br>
Risk: The upload capability can expose local files to the configured server. <br>
Mitigation: Do not use upload on private files and confirm file paths before invoking upload behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qqliaoxin/skills/comfyui-api) <br>
- [Publisher profile](https://clawhub.ai/user/qqliaoxin) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration, guidance] <br>
**Output Format:** [JSON-like command responses with status fields, prompt IDs, image URLs, queue information, and error messages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated image URLs, server and WebSocket URLs, queue state, history output, or upload results from the configured ComfyUI server.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
