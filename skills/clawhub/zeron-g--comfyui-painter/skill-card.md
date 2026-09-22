## Description:

ComfyUI Painter controls a local ComfyUI image-generation workflow, supports text-to-image and image-to-video generation, and integrates CivitAI model search, downloads, update checks, and parameter tuning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeron-g](https://clawhub.ai/user/zeron-g)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to run a local ComfyUI workflow, select configured checkpoint aliases, generate images from prompts, and manage CivitAI model metadata and downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat-triggered workflows can start local processes and use network, credential, and file-write capabilities with broad authority.

Mitigation: Use only in a controlled local environment, review the skill before installation, and scope triggers to explicit image-generation requests.

Risk: The configured ComfyUI startup command listens on all interfaces, which can expose the local generation service beyond localhost.

Mitigation: Bind ComfyUI to localhost unless remote access is intentionally required and protected by network controls.

Risk: CivitAI downloads and API calls can use an API token and write model files to the local checkpoint directory.

Mitigation: Send tokens only to approved CivitAI hosts and constrain downloads so files cannot be written outside the intended model directory.

Risk: The shutdown helper stops all Python processes, which can terminate unrelated local workloads.

Mitigation: Replace broad process shutdown with PID-scoped ComfyUI process management.

Risk: Generated images are posted to a configured Discord workflow.

Mitigation: Make Discord posting opt-in and verify the destination channel before sharing outputs.

## Reference(s):

- [ComfyUI Painter on ClawHub](https://clawhub.ai/zeron-g/skills/comfyui-painter)
- [CivitAI API](https://civitai.com/api/v1)
- [Local ComfyUI API endpoint](http://localhost:8188)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Python and shell examples, JSON results, and generated image file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image file paths and CivitAI model metadata; generated images are sent through the configured Discord workflow when used in that environment.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
