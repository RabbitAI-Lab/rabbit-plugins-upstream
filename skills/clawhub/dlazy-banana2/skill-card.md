## Description: <br>
Generate and edit high-quality images with Nano Banana 2.0 using the dLazy CLI, supporting text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users use this skill to call dLazy's hosted Nano Banana 2.0 image generation and editing service from an agent, passing prompts and optional image references through the pinned CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and any local media paths passed to the CLI can be uploaded to dLazy's hosted API and media storage. <br>
Mitigation: Use the skill only when external cloud image processing is acceptable, and avoid sending sensitive prompts or media unless approved. <br>
Risk: Authentication stores a dLazy API key locally or uses the DLAZY_API_KEY environment variable. <br>
Mitigation: Protect local CLI configuration and environment variables, and rotate or revoke the API key from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana2) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with bash commands; CLI responses are JSON containing hosted image output URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; prompts and local media paths may be sent to dLazy-hosted API and file services.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
