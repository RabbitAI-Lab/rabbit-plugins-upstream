## Description: <br>
Generates ElevenLabs eleven_v3 text-to-speech through the dLazy CLI with curated multilingual voices and stability, similarity, and style controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content creators use this skill to ask an agent to run dLazy's ElevenLabs text-to-speech command, select a supported voice, and receive a generated output URL or asynchronous task result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt text and selected parameters are sent to dLazy's hosted API for generation. <br>
Mitigation: Avoid sending sensitive or regulated content unless the user is comfortable with dLazy handling it. <br>
Risk: The default login flow stores a dLazy API key in the local CLI configuration. <br>
Mitigation: Use npx @dlazy/cli@1.2.3 or the DLAZY_API_KEY environment variable when less local persistence is preferred. <br>
Risk: Generated files are hosted by dLazy and returned as external URLs. <br>
Mitigation: Review sharing, retention, and access expectations before using generated outputs in sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; results may include hosted file URLs or asynchronous task IDs.] <br>

## Skill Version(s): <br>
1.3.4 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
