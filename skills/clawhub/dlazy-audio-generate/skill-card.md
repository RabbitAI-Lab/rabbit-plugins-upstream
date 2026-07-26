## Description: <br>
Audio generation skill that selects an appropriate dlazy CLI audio or text-to-speech model based on the user's prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate speech, music, sound effects, dialogue, or cloned-voice audio through the dLazy hosted CLI service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, generation parameters, and media files supplied for audio or voice cloning may be uploaded to dLazy hosted services. <br>
Mitigation: Avoid sending sensitive prompts or media, and use the service only when cloud processing is acceptable. <br>
Risk: Using login or manual authentication can persist an API key in the local dLazy CLI configuration. <br>
Mitigation: Use per-invocation DLAZY_API_KEY or npx when less persistent setup is preferred, and rotate or revoke API keys as needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated audio is returned through hosted result URLs from the dLazy service.] <br>

## Skill Version(s): <br>
1.3.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
