## Description: <br>
Agentvibes Voice Skill Free provides Piper-based text-to-speech support for agent voice announcements, including voice selection, preview, sampling, and speed control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add basic offline Piper TTS voice output, select or preview voices, and adjust speaking speed for simple agent announcements or content narration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command execution while describing automatic installation behavior. <br>
Mitigation: Require confirmation before Piper installation or other command execution, and review commands before allowing them in controlled environments. <br>
Risk: The skill may download Piper voice files from HuggingFace during first use. <br>
Mitigation: Confirm voice downloads before use and avoid deployment where offline-only or tightly controlled network access is required. <br>
Risk: The artifact mentions API key configuration even though the security evidence says the service need is insufficiently scoped. <br>
Mitigation: Do not provide an API key unless the publisher explains the required service and how the key is used. <br>
Risk: The optional callback_url could send completion data to an external endpoint. <br>
Mitigation: Avoid callback_url unless the destination and transmitted data are understood and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentvibes-voice-skill-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline command examples and JSON-like execution results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger local Piper installation or HuggingFace voice downloads when used as described by the artifact.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
