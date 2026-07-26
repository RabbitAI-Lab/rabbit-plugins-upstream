## Description: <br>
Promitheus gives AI agents a persistent emotional state that can be updated during work and restored across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shellbymolt](https://clawhub.ai/user/shellbymolt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to connect an OpenClaw plugin that records mood, valence, energy, arousal, and event summaries so an agent can carry state between sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally writes local emotional state and can feed that state back into future prompts. <br>
Mitigation: Install it only when persistent generated state is desired, keep STATE.md visible and easy to clear, and avoid putting sensitive information into event summaries. <br>


## Reference(s): <br>
- [OpenClaw Promitheus npm package](https://npmjs.com/package/openclaw-promitheus) <br>
- [ClawHub skill page](https://clawhub.ai/shellbymolt/skills/promitheus) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline shell commands, YAML configuration, and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The connected plugin may write STATE.md and feed that local state into future agent context.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
