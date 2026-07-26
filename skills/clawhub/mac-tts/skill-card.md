## Description: <br>
Mac TTS helps agents use the macOS built-in `say` command to read text aloud through system speakers with voice selection and volume-control examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kalijason](https://clawhub.ai/user/kalijason) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to create audible macOS notifications, alerts, reminders, and spoken messages through the local system speakers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make the local Mac speak aloud, which may reveal text in shared or quiet environments. <br>
Mitigation: Use it only when audible speech is intended, and review spoken text before running the `say` command. <br>
Risk: Volume-changing commands can alter the user's local audio settings. <br>
Mitigation: Review any `osascript` volume or mute command before execution, especially on shared devices. <br>
Risk: The documented commands are macOS-specific. <br>
Mitigation: Deploy only on macOS hosts with the built-in `say` and `osascript` commands available. <br>


## Reference(s): <br>
- [Mac TTS ClawHub skill page](https://clawhub.ai/kalijason/skills/mac-tts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS-only guidance for local text-to-speech and system volume commands] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
