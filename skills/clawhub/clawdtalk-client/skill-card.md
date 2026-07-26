## Description: <br>
ClawdTalk enables voice calls, SMS messaging, and AI Missions for Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dcasem](https://clawhub.ai/user/dcasem) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use ClawdTalk to connect Clawdbot or OpenClaw agents to phone calls, SMS, approval requests, and outbound mission workflows through ClawdTalk and Telnyx. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice transcripts, SMS content, mission data, and tool results are sent to clawdtalk.com and Telnyx-operated services. <br>
Mitigation: Install only when that data sharing is acceptable, avoid sensitive conversations unless approved, and prefer environment variables for API keys. <br>
Risk: The remote phone and SMS bridge can send requests into the user's main agent session, and the security evidence notes approval behavior that can fail open. <br>
Mitigation: Review the sessions_send gateway allowlist change, avoid untrusted callers or SMS senders, and isolate the skill to a lower-privilege agent or session until approval behavior is verified. <br>
Risk: skill-config.json may contain live API keys and gateway tokens. <br>
Mitigation: Use environment variable references where possible, restrict local file access, and rotate credentials if the configuration file is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dcasem/skills/clawdtalk-client) <br>
- [ClawdTalk client homepage](https://github.com/team-telnyx/clawdtalk-client) <br>
- [ClawdTalk](https://clawdtalk.com) <br>
- [Clawdbot](https://clawdbot.com) <br>
- [Telnyx](https://telnyx.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, JSON configuration snippets, and command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local scripts that connect to ClawdTalk, update gateway allowlists with confirmation, and manage skill-config.json.] <br>

## Skill Version(s): <br>
2.0.5 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
