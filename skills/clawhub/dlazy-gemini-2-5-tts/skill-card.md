## Description: <br>
Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate Chinese or English text-to-speech audio through the dLazy CLI, choosing a prompt and voice for cloud generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local media paths may be processed by dLazy's hosted API and media storage. <br>
Mitigation: Use only prompts and files appropriate for third-party cloud processing, and confirm the user intends to send them before invocation. <br>
Risk: The dLazy API key may be stored in the local CLI configuration. <br>
Mitigation: Prefer per-invocation environment variables for temporary use, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The skill documentation shows an output schema mismatch for this text-to-speech workflow. <br>
Mitigation: Inspect the actual CLI JSON response at runtime before downstream processing and avoid assuming the documented image-oriented example is authoritative. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts) <br>
- [Publisher profile](https://clawhub.ai/user/dlazyai) <br>
- [dLazy CLI homepage from skill metadata](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package from skill metadata](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; command responses are JSON containing hosted generation result URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; prompts are sent to api.dlazy.com and generated assets are hosted on files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
