## Description: <br>
Alibaba Bailian qwen3-tts text-to-speech that lets agents choose curated system voices, including dialects, or design a custom voice from a natural-language description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request qwen3-tts speech generation through the dLazy CLI, selecting a preset voice or describing a custom voice for text-to-speech output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TTS prompts and any explicitly provided media inputs are sent to dLazy's hosted service. <br>
Mitigation: Use the skill only when sending those inputs to dLazy is acceptable for the user's data handling requirements. <br>
Risk: The dLazy API key can authorize paid SaaS usage if exposed. <br>
Mitigation: Prefer DLAZY_API_KEY for temporary sessions on shared machines, verify permissions on ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard after suspected exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated speech result is returned through dLazy-hosted output URLs; asynchronous runs may return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
