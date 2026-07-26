## Description: <br>
Speak responses aloud on macOS using the built-in `say` command when user input indicates Voice Wake/voice recognition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xadenryan](https://clawhub.ai/user/xadenryan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and users of macOS voice-triggered agent workflows use this skill to have assistant responses spoken aloud when the latest message starts with the configured Voice Wake recognition phrase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audible responses may disclose sensitive conversation content in shared spaces. <br>
Mitigation: Install and use the skill only on macOS systems where audible assistant responses are wanted, and avoid the voice trigger for sensitive conversations in shared spaces. <br>
Risk: The local `say` command may be unavailable or fail on unsupported systems. <br>
Mitigation: Continue with a text response and notify the user that text-to-speech failed or is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xadenryan/skills/clawdbot-skill-voice-wake-say) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local macOS text-to-speech through `say` when the trigger phrase is present; otherwise responds with text only.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
