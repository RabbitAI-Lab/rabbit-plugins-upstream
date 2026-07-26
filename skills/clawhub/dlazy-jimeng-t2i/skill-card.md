## Description: <br>
Generates images from text prompts with Jimeng through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to generate Jimeng text-to-image outputs through dLazy, optionally supplying reference images and size parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dLazy API key is stored locally in the CLI configuration. <br>
Mitigation: Use per-invocation credentials where appropriate, keep config file permissions restricted to the OS user, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Prompts and selected local files can be sent to dLazy API and media storage endpoints. <br>
Mitigation: Pass only intended prompts and files, avoid sensitive inputs unless approved for external processing, and use dry-run or explicit invocation before executing generation. <br>
Risk: Pipe references such as @stdin and @* can forward broad upstream context. <br>
Mitigation: Avoid broad pipe references unless the forwarded content is understood; prefer explicit prompt and file arguments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [CLI commands and JSON responses containing generated image URLs or async task identifiers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; local media paths passed as inputs may be uploaded to dLazy storage.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
