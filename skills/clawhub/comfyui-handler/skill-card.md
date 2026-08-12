## Description:

Comfyui Handler connects an agent to a configured ComfyUI server for template-based image generation, image editing, asset upload, result polling, and local result retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1878212](https://clawhub.ai/user/1878212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send prompts and optional source images to a configured ComfyUI server, run template workflows for image generation or editing, and retrieve generated files into the workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote ComfyUI server can influence downloaded filenames and may write files outside the intended output folder.

Mitigation: Use only trusted ComfyUI hosts, avoid shared or untrusted servers, and add filename sanitization before broader deployment.

Risk: Prompts and input images are sent to the configured ComfyUI host.

Mitigation: Confirm the host and data sensitivity before running workflows with private or regulated content.

Risk: Generated outputs may be forwarded through messaging plugins or opened locally.

Mitigation: Require explicit confirmation before forwarding generated files or opening local outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1878212/skills/comfyui-handler)
- [Publisher Profile](https://clawhub.ai/user/1878212)
- [README](artifact/README.md)
- [Agent Skill Instructions](artifact/SKILL.md)
- [Text-to-Image Workflow](artifact/workflows/image_z_image_turbo.json)
- [Image Editing Workflow](artifact/workflows/qwen_image_edit_2511.json)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [JSON status messages, local file paths, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runtime outputs are generated image files saved to the local workspace after ComfyUI job polling completes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact manifest reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
