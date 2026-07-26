## Description: <br>
Generate matching scene sound effects from text descriptions or video frames using Kling SFX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate sound effects or background audio cues for scenes from prompts or a single reference video through the dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local media paths supplied to the skill may be uploaded to the dLazy cloud API and media storage. <br>
Mitigation: Avoid submitting sensitive prompts or media unless the user's workflow permits cloud processing by dLazy. <br>
Risk: The dLazy API key may be stored in the local CLI configuration. <br>
Mitigation: Use normal secret-handling practices, restrict local config access, and rotate or revoke the key from the dLazy dashboard when needed. <br>
Risk: The documented sample output shows image/png even though this is an audio sound-effect skill. <br>
Mitigation: Validate actual CLI outputs in the target workflow and treat the sample output format as inaccurate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-keling-sfx) <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON result envelopes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return asynchronous task identifiers or hosted media URLs from files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
