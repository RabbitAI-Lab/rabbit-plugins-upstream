## Description: <br>
Wyoming Protocol bridge for Home Assistant voice assistant integration with Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vglafirov](https://clawhub.ai/user/vglafirov) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and home automation operators use this skill to connect Home Assistant Assist voice transcripts to Clawdbot and return Clawdbot responses through Home Assistant text-to-speech. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bridge exposes voice prompts through an unauthenticated Wyoming Protocol listener. <br>
Mitigation: Run it only on a trusted, firewalled host and restrict network access so only Home Assistant can reach the listener. <br>
Risk: The Docker deployment shares the local Clawdbot profile with the service. <br>
Mitigation: Use a dedicated low-privilege Clawdbot profile and mount the profile read-only when feasible. <br>
Risk: Voice transcripts and assistant responses may be logged or retained in conversation context. <br>
Mitigation: Reduce or disable transcript logging and review Clawdbot retention behavior before use. <br>


## Reference(s): <br>
- [Home Assistant Assist Voice Control](https://www.home-assistant.io/voice_control/) <br>
- [Wyoming Protocol](https://github.com/rhasspy/wyoming) <br>
- [Clawdbot](https://clawd.bot) <br>
- [ClawHub Skill Page](https://clawhub.ai/vglafirov/skills/wyoming-clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python code, and Docker Compose configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and operation guidance for a local Wyoming Protocol bridge that invokes the Clawdbot CLI.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
