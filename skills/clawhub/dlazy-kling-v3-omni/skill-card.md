## Description: <br>
Versatile video generation with Kling v3 Omni, supporting multi-modal image and prompt inputs for dynamic video generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to call the dLazy Kling v3 Omni CLI for text-to-video and image or video reference generation workflows, including synchronous generation and asynchronous task polling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local media paths supplied to the CLI can be uploaded to dLazy's hosted service. <br>
Mitigation: Use the skill only with content approved for dLazy cloud processing and avoid sending sensitive media or confidential prompts unless the user's policy permits it. <br>
Risk: The dLazy CLI may save an API key in the local user configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni) <br>
- [dLazy Homepage](https://dlazy.com) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted output URLs or an asynchronous task identifier.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
