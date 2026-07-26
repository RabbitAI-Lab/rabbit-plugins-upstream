## Description: <br>
Synthesize text into natural and fluent speech using Doubao TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to authenticate with dLazy and generate Chinese or English text-to-speech audio through the pinned dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected parameters are sent to dLazy's hosted API. <br>
Mitigation: Avoid sensitive prompts unless the dLazy service is trusted for the intended use. <br>
Risk: A persistent global CLI install may be undesirable on shared or tightly controlled systems. <br>
Mitigation: Use the documented npx invocation when a non-persistent CLI execution path is preferred. <br>
Risk: The skill's output example appears to use an image schema instead of an audio schema. <br>
Mitigation: Verify returned result types before relying on generated outputs in downstream workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Files, Guidance] <br>
**Output Format:** [Markdown instructions with CLI commands and JSON result metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted generated output URLs; async mode can return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
