## Description: <br>
Comfy Cloud connects an agent to the hosted Comfy Cloud MCP server to generate images, video, audio, and 3D assets, search models and workflow templates, run custom ComfyUI workflows, and manage generation jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mattmillerai](https://clawhub.ai/user/mattmillerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure OpenClaw for Comfy Cloud and request generation or editing of images, video, audio, 3D assets, and ComfyUI workflows through the hosted MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and uploaded files may be sent to Comfy Cloud for hosted processing. <br>
Mitigation: Only upload content that is appropriate for Comfy Cloud processing and review account, privacy, and content policies before use. <br>
Risk: API keys can be exposed if copied into shared files or transcripts. <br>
Mitigation: Use OAuth when possible; for headless use, keep COMFY_API_KEY in environment or secret storage and avoid committing or sharing it. <br>
Risk: Generation requests may consume Comfy Cloud credits. <br>
Mitigation: Confirm the intended model, workflow, and input files before submitting jobs, especially batch or high-cost generation requests. <br>


## Reference(s): <br>
- [Comfy Cloud MCP docs](https://docs.comfy.org/cloud/mcp) <br>
- [Comfy Cloud](https://cloud.comfy.org) <br>
- [ComfyUI](https://www.comfy.org) <br>
- [ClawHub skill page](https://clawhub.ai/mattmillerai/skills/comfy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and MCP tool-selection guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Comfy Cloud job and output URLs through the configured MCP server; generation can consume Comfy Cloud credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
