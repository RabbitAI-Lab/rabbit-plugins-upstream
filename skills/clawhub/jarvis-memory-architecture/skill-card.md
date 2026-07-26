## Description: <br>
Universal memory architecture for AI agents. Provides long-term memory, daily logs, diary, cron inbox, heartbeat state tracking, social platform post tracking, sub-agent context patterns, and adaptive learning -- everything an agent needs for identity continuity across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psychotechv4](https://clawhub.ai/user/psychotechv4) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to set up local file-based memory for identity continuity, daily logs, inter-session messages, heartbeat state, platform post tracking, and adaptive strategy notes across agent sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory files may accumulate sensitive personal or operational context. <br>
Mitigation: Treat memory files as private, review them regularly, and avoid storing secrets, credentials, or precise credential locations. <br>
Risk: Loading memory in shared, public, or untrusted agent contexts could expose private context. <br>
Mitigation: Only auto-load memory in trusted main sessions and disable memory loading for shared or untrusted contexts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psychotechv4/skills/jarvis-memory-architecture) <br>
- [Publisher profile](https://clawhub.ai/user/psychotechv4) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration instructions, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory file templates and operating routines for agent sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
