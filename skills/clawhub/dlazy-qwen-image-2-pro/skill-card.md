## Description: <br>
Generates images with Alibaba Bailian qwen-image-2.0-pro through the dLazy CLI, supporting prompts, reference images, size selection, prompt rewriting, dry-run cost estimates, and asynchronous task polling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to call dLazy's hosted qwen-image-2-pro image generation service from an agent workflow. It is intended for creating image outputs from prompts and optional reference images while receiving structured CLI results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local files are sent to dLazy's hosted service for generation. <br>
Mitigation: Avoid sending sensitive prompts or confidential files unless the dLazy service terms and organizational policy allow it. <br>
Risk: The CLI stores an API key in the user's local configuration unless the key is supplied per invocation. <br>
Mitigation: Use the DLAZY_API_KEY environment variable or npx for ephemeral use, and rotate or revoke the key from the dLazy dashboard when access changes. <br>
Risk: Generated outputs are hosted by dLazy and returned as files.dlazy.com URLs. <br>
Mitigation: Treat returned URLs according to data handling requirements before sharing or embedding them in downstream workflows. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro) <br>
- [Publisher profile](https://clawhub.ai/user/dlazyai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [CLI commands and JSON responses containing generated image URLs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
