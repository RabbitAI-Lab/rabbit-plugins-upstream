## Description: <br>
Control and monitor Tesla vehicles through the Tessie API for battery status, range, location, charging, climate, drive history, idles, and FSD statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baanish](https://clawhub.ai/user/baanish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users with a Tessie account use this skill to let an agent retrieve Tesla vehicle telemetry and submit Tessie API commands for climate, charging, and vehicle status workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access live vehicle telemetry, including precise location and vehicle metadata. <br>
Mitigation: Install only when the user trusts the skill with a Tessie API key, and avoid sharing command output that may include location or vehicle details. <br>
Risk: The skill can issue remote vehicle commands such as climate and charging actions. <br>
Mitigation: Review agent-proposed commands before execution, especially commands that affect vehicle state or user safety. <br>
Risk: A Tessie API key grants access to sensitive account and vehicle operations. <br>
Mitigation: Keep the key out of shared files and logs, store it only in the intended configuration or environment variable, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Tessie Developer Setup](https://tessie.com/developers) <br>
- [Tessie API Documentation](https://developer.tessie.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/baanish/skills/tessie) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Tessie API credentials from configuration or environment variables and may return live vehicle telemetry.] <br>

## Skill Version(s): <br>
2.0.3 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
