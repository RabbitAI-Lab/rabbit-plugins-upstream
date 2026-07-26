## Description: <br>
Dlazy Videoretalk helps an agent invoke dLazy's Tongyi VideoRetalk service to regenerate a talking-person video so the speaker's mouth movement matches a supplied audio track, with optional reference-face selection for videos containing multiple people. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call dLazy's hosted VideoRetalk workflow for lip-syncing a person video to a new voice audio track. It is suited for cloud media-generation tasks where the user provides video, audio, and optionally a reference face image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected local video, audio, and image files may be uploaded to dLazy for processing. <br>
Mitigation: Install and use the skill only when sending those media files to dLazy is acceptable for the user's workflow. <br>
Risk: The skill stores a dLazy organization API key locally, and the inspected evidence does not clearly confirm enforcement of the claimed permission protections. <br>
Mitigation: Prefer passing DLAZY_API_KEY per invocation, verify that any saved config file is readable only by the current user, and rotate or revoke keys from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [Dlazy Videoretalk on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted media URLs or asynchronous task identifiers from dLazy.] <br>

## Skill Version(s): <br>
1.3.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
