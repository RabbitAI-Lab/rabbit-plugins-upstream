## Description: <br>
Generate Flux 2 Klein images through the RunComfy CLI, with model-specific prompting, variant-selection, step-count, and output-handling guidance for fast concepting and polished image generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and creative agents use this skill to route image-generation requests to Flux 2 Klein on RunComfy, choose the 4B or 9B variant, and produce CLI calls and prompt guidance for rapid visual iteration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference-image inputs are sent to RunComfy for hosted image generation. <br>
Mitigation: Use the skill only when the user is comfortable sharing those inputs with RunComfy, and avoid sending sensitive or unapproved content. <br>
Risk: The skill depends on the RunComfy CLI account flow and token handling. <br>
Mitigation: Install the CLI from a trusted source, use RUNCOMFY_TOKEN in CI when a local token file is undesirable, and protect local RunComfy configuration files. <br>
Risk: Generated media can be incorrect, unsafe, or unsuitable for the intended use. <br>
Mitigation: Review generated images and associated prompts before publication or downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/flux-2-klein) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [Flux 2 Klein 9B model](https://www.runcomfy.com/models/blackforestlabs/flux-2-klein/9b/text-to-image?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-2-klein) <br>
- [Flux 2 Klein 4B model](https://www.runcomfy.com/models/blackforestlabs/flux-2-klein/4b/text-to-image?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-2-klein) <br>
- [RunComfy CLI introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-2-klein) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-2-klein) <br>
- [RunComfy models catalog](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-2-klein) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides RunComfy CLI invocations that return JSON status/results and downloaded generated image files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
