## Description: <br>
Generate dynamic videos from a first-frame image and prompt using the dLazy Jimeng image-to-video command. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to call dLazy's hosted Jimeng image-to-video service with a prompt and first-frame image, then receive generated media output or asynchronous task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, parameters, and local media files may be sent to dLazy's hosted API and media storage. <br>
Mitigation: Confirm with the user before uploading local files, and avoid sending sensitive prompts or media unless the user accepts dLazy cloud processing. <br>
Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable. <br>
Mitigation: Use the documented dLazy authentication flow, protect the local config file and environment, and rotate or revoke the key from the dLazy dashboard when needed. <br>
Risk: The documented examples use --image even though the command options expose --firstFrame for this first-frame video workflow. <br>
Mitigation: Prefer --firstFrame for agent-generated commands and use dry-run or help output when confirming parameters. <br>
Risk: Cloud generation may spend dLazy credits and can fail for insufficient balance or authorization errors. <br>
Mitigation: Use --dry-run when cost awareness is needed, and surface insufficient-balance or unauthorized errors with the relevant dLazy dashboard action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Media URLs, Guidance] <br>
**Output Format:** [JSON response with generated media URLs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a pinned @dlazy/cli command; --no-wait returns a generateId for later polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
