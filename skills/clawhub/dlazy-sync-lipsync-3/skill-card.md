## Description: <br>
fal.ai sync-lipsync v3 generates a new video whose speaker lip movements match a supplied audio track, for dubbing, localization, and virtual presenter re-syncing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative production teams use this skill to invoke dLazy's hosted sync-lipsync-3 service from an agent workflow, supplying a video and audio track to generate lip-synced video output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads user-provided video and audio files to dLazy's hosted service for processing. <br>
Mitigation: Use only media that is approved for processing by dLazy, and avoid submitting sensitive content unless the user has accepted that transfer. <br>
Risk: Authentication can persist a dLazy API key in the local CLI configuration. <br>
Mitigation: Use the DLAZY_API_KEY environment variable or npx path when less local persistence is preferred, and rotate or revoke the key from dLazy when needed. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files] <br>
**Output Format:** [Markdown instructions with bash commands and CLI JSON output containing generated media URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return an asynchronous task identifier when no-wait mode is used.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
