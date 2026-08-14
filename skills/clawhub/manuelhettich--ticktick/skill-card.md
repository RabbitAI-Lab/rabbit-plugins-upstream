## Description: <br>
Manage TickTick tasks and projects from the command line with OAuth2 auth, batch operations, and rate limit handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manuelhettich](https://clawhub.ai/user/manuelhettich) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to authenticate to TickTick, list tasks and projects, and create, update, complete, or abandon tasks from command-line workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change TickTick tasks and projects. <br>
Mitigation: Require explicit approval before task mutations such as complete, abandon, batch-abandon, or project updates. <br>
Risk: OAuth client secrets and tokens are stored in a plaintext local config file. <br>
Mitigation: Protect ~/.clawdbot/credentials/ticktick-cli/config.json, avoid syncing or exposing it, and revoke the TickTick app if credentials leak. <br>
Risk: Bulk or repeated operations can hit TickTick API rate limits. <br>
Mitigation: Use batch operations deliberately and wait before retrying when the API reports rate limiting. <br>


## Reference(s): <br>
- [TickTick Developer Center](https://developer.ticktick.com/manage) <br>
- [TickTick Open API v1](https://developer.ticktick.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read or mutate TickTick tasks and projects after OAuth authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
