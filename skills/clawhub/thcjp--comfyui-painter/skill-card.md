## Description: <br>
Comfyui Painter connects an agent to local ComfyUI and CivitAI workflows for image generation, image-to-video generation, model search and downloads, recommended-parameter extraction, and local configuration caching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, content production teams, and automation developers use this skill to run local GPU image-generation workflows through ComfyUI while managing CivitAI model metadata, downloads, and prompt parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local ComfyUI commands and update local config.json. <br>
Mitigation: Require explicit user confirmation before executing local commands or changing configuration, and review generated or modified files before relying on them. <br>
Risk: The skill can use a CivitAI API key and download large model files. <br>
Mitigation: Keep credentials out of version control and logs, confirm each model download and source before starting it, and review storage and licensing implications. <br>
Risk: The security review notes prompt-expansion guidance that can add explicit sexual prompt terms without clear opt-in. <br>
Mitigation: Remove or constrain that behavior unless adult-content generation is intentionally enabled, explicitly confirmed, and policy-compliant. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/comfyui-painter) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [CivitAI](https://civitai.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline Python and shell examples, plus generated asset paths or JSON-style execution results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call local ComfyUI and CivitAI APIs, download large model files, and update local configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter lists 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
