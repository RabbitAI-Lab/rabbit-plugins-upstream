## Description: <br>
AI Image Gen helps agents generate and edit images by preparing prompts, selecting Gemini Flash Image model variants, and saving generated image outputs locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, designers, marketers, and developers use this skill to generate commercial image assets, transform reference images, choose aspect ratios and resolutions, and obtain local PNG output paths through an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference images may be sent to a configured Gemini-compatible image API. <br>
Mitigation: Use the skill only with data approved for that external service, and avoid confidential prompts or images unless the service terms and data handling controls are acceptable. <br>
Risk: The image generation API key could be exposed if entered into chat, logs, scripts, or generated image metadata. <br>
Mitigation: Keep the API key in environment variables, do not paste it into agent prompts, and review generated commands before execution. <br>
Risk: The artifact references a generation script that is not included in the submitted files. <br>
Mitigation: Verify the actual runtime script and its network, file-write, and command-execution behavior before production or confidential use. <br>
Risk: Generated image outputs are saved locally and may contain content subject to third-party service terms. <br>
Mitigation: Choose appropriate output paths, review generated content before reuse, and confirm commercial usage rights with the image service provider. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/thcjp/skills/ai-image-gen) <br>
- [Configured Gemini-compatible image API endpoint](https://code.newcli.com/gemini) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated PNG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save PNG outputs locally; accepts a prompt, model identifier, output path, and optional reference image path.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
