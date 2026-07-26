## Description: <br>
Generate high-quality images with Vidu Q2, including text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to invoke dLazy's hosted Vidu Q2 image generation service for prompt-based image creation and image-conditioned edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local image inputs may be uploaded to dLazy's hosted service. <br>
Mitigation: Avoid submitting sensitive prompts or files unless the deployment's data-handling requirements allow use of dLazy's hosted API. <br>
Risk: The dLazy CLI can store an API key in the local user configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Broad image-generation requests could trigger the skill unintentionally. <br>
Mitigation: Invoke it explicitly with Vidu Q2 or dLazy terms, matching the security guidance's overbroad-trigger caution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image outputs are returned as hosted URLs; asynchronous requests may return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
