## Description: <br>
Generate customized speech that highly restores the timbre by uploading reference audio using Kling Audio Clone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke dLazy's Kling Audio Clone service for custom voice generation from reference audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference audio is uploaded to a third-party voice-cloning service. <br>
Mitigation: Use the skill only with audio you have rights or consent to submit, and avoid sensitive or private voice samples unless the service terms and data handling are acceptable. <br>
Risk: The skill stores or uses a dLazy API key for authenticated service calls. <br>
Mitigation: Store credentials only in the documented local config or per-invocation environment variable, rotate or revoke keys when access changes, and avoid sharing logs that may expose credentials. <br>
Risk: The current documentation has inconsistent examples and output type details. <br>
Mitigation: Run `dlazy kling-audio-clone -h` and verify required arguments, response shape, and async behavior before relying on the skill in an automated workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-audio-clone) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses dLazy API credentials and may return hosted media URLs or asynchronous task identifiers.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
