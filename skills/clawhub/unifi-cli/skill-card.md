## Description: <br>
Use this skill to answer questions about UniFi network gear and local network clients by querying a local UniFi gateway through the unifi CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baileywickham](https://clawhub.ai/user/baileywickham) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, administrators, and support agents use this skill to inspect UniFi devices, sites, network application version, and connected clients on a local UniFi gateway. It also guides agents to request explicit confirmation before disruptive restart or power-cycle actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a local UniFi API key and may reveal client or device inventory from a private network. <br>
Mitigation: Install and run it only in trusted environments, keep the API key protected, and treat returned network inventory as sensitive data. <br>
Risk: Restart and power-cycle commands can intentionally disrupt UniFi network equipment. <br>
Mitigation: Run disruptive commands only after the user explicitly confirms the specific action in the conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baileywickham/skills/unifi-cli) <br>
- [Bun](https://bun.sh) <br>
- [unifi-cli project referenced by artifact](https://github.com/baileywickham/unifi-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill recommends JSON output when command results need to be parsed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
