## Description: <br>
Generate coherent transition videos using Jimeng's first and tail frame models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users use this skill to call dLazy's hosted Jimeng first-and-last-frame video workflow from an agent, providing a prompt plus first and last frame images to generate transition video output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local first or last frame images are sent to dLazy's hosted service for generation. <br>
Mitigation: Use the skill only when cloud processing by dLazy is intended, and avoid sending sensitive prompts or media unless that use is acceptable for the user's environment. <br>
Risk: Broad trigger wording could make the skill run for generic transition-video requests. <br>
Mitigation: Confirm that the user intends to use dLazy's Jimeng video service before invoking the command. <br>
Risk: Authentication can persist a dLazy API key in the local CLI configuration. <br>
Mitigation: Use per-invocation DLAZY_API_KEY or npx when a less persistent setup is preferred, and rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, json, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return generated media URLs or an asynchronous task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
