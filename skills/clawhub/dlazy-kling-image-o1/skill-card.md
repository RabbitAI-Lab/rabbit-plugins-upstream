## Description: <br>
Generate exquisite images with the Kling o1 model, supporting text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke the dLazy CLI for Kling o1 image generation from prompts and optional reference images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and referenced local image files are sent to dLazy services for image generation. <br>
Mitigation: Install and invoke the skill only when this data transfer is intended; use dry-run when available to review payload and cost before calling the API. <br>
Risk: The skill stores a dLazy API key locally, and scanner evidence notes that inspected CLI code may not enforce the restricted file permissions claimed by the skill. <br>
Mitigation: Prefer per-invocation DLAZY_API_KEY in sensitive environments, or check and restrict permissions on ~/.dlazy/config.json after login or auth set. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1) <br>
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the dLazy CLI to return hosted image output URLs or asynchronous task status.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
