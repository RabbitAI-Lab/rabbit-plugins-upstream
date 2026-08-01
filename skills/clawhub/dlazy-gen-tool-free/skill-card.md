## Description: <br>
综合生成工具-免费版 helps personal creators generate and edit images through the dlazy CLI, including text-to-image, foreground separation, and super-resolution workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual creators and developers use this skill to configure dlazy and run image generation, basic image editing, foreground separation, and super-resolution commands for creative prototypes and visual assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses broad agent activation and persistent third-party CLI/API-key access without a tight privacy disclosure. <br>
Mitigation: Use it only for image-generation tasks, avoid private prompts or confidential assets unless dlazy is approved for that data, and store the API key in an environment variable or carefully permissioned config. <br>
Risk: Prompts, source images, and generated assets may be processed by a third-party service. <br>
Mitigation: Review inputs before execution, avoid unreleased product images or sensitive creative briefs, and confirm dlazy data-handling approval for the intended workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dlazy-gen-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline shell and Python examples plus JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16+, @dlazy/cli, and a dlazy API key; outputs may include hosted image URLs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
