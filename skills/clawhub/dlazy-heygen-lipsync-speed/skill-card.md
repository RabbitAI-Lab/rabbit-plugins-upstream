## Description: <br>
Runs dLazy's HeyGen Lipsync Speed workflow through the dLazy CLI for fast lip-sync generation from user-supplied media. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to run a hosted lip-sync generation workflow when rapid video and audio synchronization is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dLazy CLI stores an API key in a local user configuration file when authenticated. <br>
Mitigation: Use per-invocation DLAZY_API_KEY where appropriate, and rotate or revoke organization keys from the dLazy dashboard if access changes. <br>
Risk: Video and audio inputs supplied to the command are uploaded to dLazy's hosted service for processing. <br>
Mitigation: Confirm the selected media is appropriate for third-party cloud processing before invoking the skill. <br>
Risk: A persistent global install adds a pinned third-party CLI binary to the user's environment. <br>
Mitigation: Use the pinned npx invocation when a temporary execution path is preferred. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files] <br>
**Output Format:** [JSON with generated media URLs or async task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted files.dlazy.com media URLs; async mode returns a generateId for polling.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
