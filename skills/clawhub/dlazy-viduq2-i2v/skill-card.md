## Description: <br>
Convert static images into dynamic videos using the Vidu Q2 image-to-video model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users use this skill to invoke dLazy's Vidu Q2 image-to-video CLI, supplying prompts and source images to generate hosted video outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected prompts, parameters, and media files are sent to dLazy services for generation. <br>
Mitigation: Confirm the user is comfortable sending the selected inputs to dLazy before invoking the CLI. <br>
Risk: A dLazy API key may be stored in the local CLI configuration. <br>
Mitigation: Use per-invocation DLAZY_API_KEY when persistent storage is not desired, and rotate or revoke keys from the dLazy dashboard when they are no longer needed. <br>
Risk: A global CLI installation persists on the system. <br>
Mitigation: Prefer the pinned npx invocation when a non-persistent CLI execution is sufficient. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted result URLs or an async generateId for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
