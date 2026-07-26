## Description: <br>
Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and external users use this skill to ask an agent to generate or transform images through the dLazy Seedream 4.5 CLI. It is suited for prompt-driven image generation and image-to-image tasks where outputs are returned as hosted image URLs or asynchronous task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local files may be sent to dLazy cloud services for generation. <br>
Mitigation: Do not pass sensitive prompts or files unless they are appropriate for dLazy processing; use dry-run mode when checking payloads before execution. <br>
Risk: The skill requires a dLazy API key that is saved in local CLI configuration or supplied through an environment variable. <br>
Mitigation: Keep the key scoped to the intended organization, protect the local config, and rotate or revoke the key from the dLazy dashboard if exposure is suspected. <br>
Risk: Generated outputs are returned as URLs hosted on files.dlazy.com. <br>
Mitigation: Treat returned URLs as externally hosted artifacts and review generated content before sharing or using it downstream. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated image URLs, or an asynchronous task identifier when no-wait mode is used.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
