## Description: <br>
Comfyui Painter Free helps agents use a local ComfyUI setup to generate text-to-image outputs with manual model and parameter controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to generate anime or realistic images through a local ComfyUI instance, manage the local ComfyUI lifecycle, and tune basic generation parameters manually. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated images can remain in the workspace temporary directory after use. <br>
Mitigation: Avoid sensitive or private image generation unless temporary workspace retention is acceptable, and clean generated outputs when they are no longer needed. <br>
Risk: The skill controls a local ComfyUI process and relies on referenced local scripts and configuration. <br>
Mitigation: Confirm the source of the ComfyUI scripts and config, then review them separately before installing or running the skill. <br>
Risk: Manual image-generation parameters can lead to timeouts or GPU memory exhaustion. <br>
Mitigation: Start with conservative resolution, batch size, and step counts, then adjust while monitoring local GPU resources. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/comfyui-painter-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with Python and shell snippets; runtime results are JSON-like status objects and generated PNG file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated images are written to the workspace temporary directory and returned as file paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
