## Description: <br>
Generate images via Sophnet Qwen-Image-Plus and poll for task completion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duffycoder](https://clawhub.ai/user/duffycoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to request image generation through Sophnet Qwen-Image-Plus, configure common generation options, and receive image URLs after task completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image prompts are sent to Sophnet for processing. <br>
Mitigation: Install and use the skill only when sending prompt content to Sophnet is intended, and avoid sensitive prompt content. <br>
Risk: Sophnet API credentials are required for generation. <br>
Mitigation: Prefer a scoped API key supplied through SOPHNET_API_KEY instead of passing credentials as command-line arguments. <br>
Risk: Generated IMAGE_URL values can include signature query parameters. <br>
Mitigation: Treat generated URLs as temporary access links and avoid unnecessary sharing or logging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duffycoder/skills/qwen-image-plus-sophnet) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text] <br>
**Output Format:** [Key-value terminal output with TASK_ID, STATUS, and IMAGE_URL lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Sophnet API key; generated image URLs may include temporary signature query parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
