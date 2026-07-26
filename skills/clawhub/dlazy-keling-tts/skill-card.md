## Description: <br>
Convert text into high-quality, emotional speech reading using Kling TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn supplied text into generated speech through the dLazy Kling TTS command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TTS prompt text is sent to dLazy for processing. <br>
Mitigation: Use the skill only for text that is appropriate to send to the dLazy service. <br>
Risk: The installed CLI may store a reusable dLazy API key in local configuration with weaker file permissions than the skill claims. <br>
Mitigation: Prefer DLAZY_API_KEY for individual invocations, or manually restrict ~/.dlazy/config.json permissions after login. <br>
Risk: The skill installs or runs the pinned third-party dLazy CLI. <br>
Mitigation: Review the pinned @dlazy/cli@1.2.3 package before global installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-keling-tts) <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files] <br>
**Output Format:** [JSON responses with generated speech output URLs and optional shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated output is hosted by dLazy and may return an asynchronous task identifier when no-wait mode is used.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
