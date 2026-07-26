## Description: <br>
Speak responses aloud on macOS using the built-in `say` command when user input indicates Voice Wake/voice recognition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xadenryan](https://clawhub.ai/user/xadenryan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an assistant speak responses aloud on macOS when the latest user message begins with the voice-recognition trigger phrase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spoken responses may be overheard in the user's environment. <br>
Mitigation: Use audible output only where it is appropriate, and keep sensitive or code-heavy details on screen when needed. <br>
Risk: Audio output depends on the macOS `say` command being available. <br>
Mitigation: If `say` is unavailable or errors, return the text response normally and note that text-to-speech failed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xadenryan/skills/voice-wake-say) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with local macOS `say` shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local macOS text-to-speech only when the latest user message starts with the voice-recognition trigger phrase.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
