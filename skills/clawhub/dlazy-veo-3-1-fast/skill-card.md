## Description: <br>
Fast response and generation of short videos with Google Veo 3.1 Fast. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to call the dLazy CLI for text-to-video, image-to-video, and video extension workflows with Google Veo 3.1 Fast. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, generation parameters, and local media paths passed to the CLI may be sent or uploaded to dLazy services. <br>
Mitigation: Invoke the skill explicitly for intended dLazy video generation tasks and confirm local file paths before running it. <br>
Risk: The CLI can store a persistent API key in the user's local configuration. <br>
Mitigation: Use DLAZY_API_KEY per invocation when persistent credential storage is not appropriate, and rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast) <br>
- [dLazy CLI](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media is returned as hosted file URLs; asynchronous runs may return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
