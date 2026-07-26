## Description: <br>
Image super-resolution tool that enhances image clarity and details and returns an enhanced image URL for restoration or upscaling workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to invoke dLazy's hosted super-resolution service on an image URL or local image path and receive an enhanced image URL. It is suited to low-resolution asset restoration and secondary upscaling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images or image URLs are sent to dLazy's hosted cloud service for processing. <br>
Mitigation: Use the skill only for images appropriate to send to dLazy, and run with --dry-run when payload and cost should be inspected before making a request. <br>
Risk: The dLazy API key may be stored in local CLI configuration or supplied through the environment. <br>
Mitigation: Prefer DLAZY_API_KEY for per-invocation use or verify permissions on ~/.dlazy/config.json on shared machines; rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [Dlazy Superres ClawHub page](https://clawhub.ai/dlazyai/skills/dlazy-superres) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [JSON response containing image output URLs, with optional shell commands and human-facing guidance for authentication or billing errors] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return a generated image URL immediately or an asynchronous task identifier when --no-wait is used.] <br>

## Skill Version(s): <br>
1.3.6 (source: artifact frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
