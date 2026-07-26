## Description: <br>
Dlazy Banana Pro lets agents generate or edit images with Nano Banana Pro through the dLazy CLI, supporting text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to request generated or edited images from dLazy's hosted Nano Banana Pro service, including prompts with optional reference images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local files may be sent to dLazy API and media storage endpoints. <br>
Mitigation: Use only data approved for dLazy processing, avoid sensitive local files unless permitted, and confirm file paths before invocation. <br>
Risk: Login stores a dLazy API key in the local CLI configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The security summary notes a minor risk of broad auto-triggering. <br>
Mitigation: Confirm user intent before running commands that upload files, call the hosted service, or consume account credits. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro) <br>
- [dLazy Homepage](https://dlazy.com) <br>
- [dLazy CLI Repository](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, images] <br>
**Output Format:** [JSON returned by the dLazy CLI, typically containing generated image URLs or an asynchronous task ID.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dLazy authentication; selected local input files may be uploaded to dLazy endpoints, and async jobs can be polled with a generateId.] <br>

## Skill Version(s): <br>
1.2.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
