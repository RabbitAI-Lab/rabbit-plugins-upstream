## Description: <br>
Powerful video generation with Kling v3 for high-quality text-to-video and image-to-video through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate videos from text prompts or image inputs via the dLazy-hosted Kling v3 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, parameters, and local media paths are sent to the dLazy hosted API and media storage. <br>
Mitigation: Use the skill only for media that may be processed by dLazy, and review inputs before invoking the CLI. <br>
Risk: The dLazy API key may be stored in the local user configuration file. <br>
Mitigation: Protect the local config file and rotate or revoke the key from the dLazy dashboard if exposure is suspected. <br>
Risk: Video generation consumes dLazy credits. <br>
Mitigation: Monitor credit usage and use dry-run or explicit parameters when cost awareness is needed. <br>


## Reference(s): <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media is returned as hosted output URLs; asynchronous runs may return a task ID for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
