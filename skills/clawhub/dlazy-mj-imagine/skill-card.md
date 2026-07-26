## Description: <br>
Midjourney style generation, supports aspect ratio, bot type, and output position for artistic and strongly stylized creative image generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to call the dLazy CLI for Midjourney-style image generation from prompts, aspect ratio settings, bot type, and grid or upsample output choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts and any explicitly referenced media files to third-party dLazy cloud services. <br>
Mitigation: Use only prompts and files approved for dLazy processing, and avoid passing sensitive or restricted local media. <br>
Risk: The skill depends on a third-party npm CLI and stores or reads dLazy API credentials for authenticated requests. <br>
Mitigation: Prefer the pinned `npx @dlazy/cli@1.2.3` command when a global install is not desired, protect `~/.dlazy/config.json`, and rotate or revoke API keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine) <br>
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai) <br>
- [dLazy CLI source link from skill metadata](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image results are returned as JSON with file URLs; asynchronous runs may return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
