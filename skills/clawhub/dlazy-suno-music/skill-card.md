## Description: <br>
Generates Suno music through the dLazy CLI, supporting inspiration mode, custom lyrics, vocals, or instrumental output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and agents use this skill to generate music through dLazy's hosted Suno music service from prompts, custom lyrics, style controls, and vocal or instrumental settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, generation parameters, and local files explicitly passed to media fields may be sent to dLazy's hosted service. <br>
Mitigation: Avoid submitting sensitive content unless approved for the third-party service and review dLazy's service terms before use. <br>
Risk: Authentication through `dlazy login` or `dlazy auth set` stores the API key in the local dLazy configuration file. <br>
Mitigation: Use `DLAZY_API_KEY` per invocation when the key should not be saved in the local config file, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The skill depends on a third-party CLI package installed through npm or run with npx. <br>
Mitigation: Review the pinned `@dlazy/cli` package and source before installation, and use the documented pinned version. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown instructions with bash commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return generated media URLs or an async generateId for later polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
