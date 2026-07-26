## Description: <br>
AgentVibes provides text-to-speech voice management for Claude Code and OpenClaw, including voice switching, personality styles, speed control, background music, language learning mode, effects, and provider selection across Piper, macOS Say, Windows SAPI, and Soprano. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulpreibisch](https://clawhub.ai/user/paulpreibisch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to control spoken output for Claude Code and OpenClaw sessions, including voice selection, narration verbosity, replay, translation, and audio effects. It is intended for local text-to-speech workflows where no account or API key is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some Piper voices may require downloads from Hugging Face before offline use. <br>
Mitigation: Confirm required voices are available and downloaded before relying on offline text-to-speech behavior. <br>
Risk: The AgentVibes runtime exposes update and cleanup commands that affect local runtime state or cached audio. <br>
Mitigation: Review the separate AgentVibes runtime before allowing update or cleanup commands. <br>
Risk: Cached spoken output may contain sensitive session content. <br>
Mitigation: Use the documented cleanup command after sessions where spoken output may include sensitive information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulpreibisch/skills/agentvibes-openclaw-skill) <br>
- [Piper voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with slash commands and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command guidance for configuring text-to-speech voices, providers, effects, replay, cleanup, and spoken-output preferences.] <br>

## Skill Version(s): <br>
4.6.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
