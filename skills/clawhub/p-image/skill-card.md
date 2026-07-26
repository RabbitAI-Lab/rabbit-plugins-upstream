## Description: <br>
Use when someone wants a fast AI image - product shots, hero visuals, mood boards, or draft photos from a text prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and external users use this skill to draft prompts, choose aspect ratios, and call Pruna's p-image model for fast text-to-image generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a disable_safety_checker option, which could bypass normal provider safety controls. <br>
Mitigation: Review the skill before installing, avoid using disable_safety_checker, and provide external tokens or custom weights only when their purpose and destination are understood. <br>


## Reference(s): <br>
- [p-image on ClawHub](https://clawhub.ai/pruna-ai/skills/p-image) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY; required input is prompt, with optional aspect ratio, seed, LoRA settings, Hugging Face token, and safety-checker control.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
