## Description: <br>
Generate images and media using the fal.ai API, including text-to-image, image editing, image-to-image, and video-to-video queue workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sxela](https://clawhub.ai/user/sxela) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to submit, validate, poll, and retrieve fal.ai media-generation jobs from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, videos, URLs, and possible audio are sent to fal.ai for processing. <br>
Mitigation: Avoid submitting sensitive or regulated media unless the user has approved that external processing. <br>
Risk: fal.ai credentials may be exposed if API keys are committed or stored in shared files. <br>
Mitigation: Prefer FAL_KEY or a dedicated local configuration and do not commit secrets to TOOLS.md. <br>
Risk: Queued job state may persist locally after media-generation requests complete. <br>
Mitigation: Keep FAL_PENDING_FILE in the OpenClaw workspace and clear fal-pending.json after sensitive jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sxela/skills/falai) <br>
- [Model schema reference](references/models.json) <br>
- [fal.ai API keys](https://fal.ai/dashboard/keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with JSON inputs, shell commands, Python examples, and fal.ai queue results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return request IDs, status JSON, result URLs, and local pending-job state.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
