## Description: <br>
Generate or edit images via Gemini 3 Pro Image (Nano Banana Pro). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dycathecorde](https://clawhub.ai/user/dycathecorde) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and image creators use this skill to generate new images, edit a single input image, or compose multiple input images with Gemini 3 Pro Image from shell commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected input images are sent to Google Gemini for processing. <br>
Mitigation: Use only prompts and images approved for third-party processing, and prefer GEMINI_API_KEY in the environment instead of passing the key on the command line. <br>
Risk: Using the skill can consume Gemini API quota and depends on uv-resolved Python packages. <br>
Mitigation: Confirm Gemini quota and billing expectations before use, and review resolved dependencies when supply-chain controls matter. <br>


## Reference(s): <br>
- [Google AI developer documentation](https://ai.google.dev/) <br>
- [ClawHub skill page](https://clawhub.ai/dycathecorde/skills/nano-banana-pro-2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated PNG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save PNG files and print a MEDIA: path for supported chat attachment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
