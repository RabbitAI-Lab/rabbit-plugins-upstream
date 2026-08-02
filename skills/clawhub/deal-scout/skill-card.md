## Description: <br>
OpenClaw Deal Scout helps solo operators run a local Gmail-to-CRM deal pipeline that classifies inbound emails with Gemini, logs confirmed deals to HubSpot, sends Discord notifications, and sends approved replies during UK business hours. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asmaiqbal01](https://clawhub.ai/user/asmaiqbal01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and small teams use this skill to configure and operate a local agent workflow that triages Gmail deal inquiries, records qualifying leads in HubSpot, alerts in Discord, and keeps replies behind an approval and UK business-hours sending policy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow requires sensitive Gmail and HubSpot account access. <br>
Mitigation: Review the cloned repository code before installation, grant the narrowest permissions that work, and protect local credential files and API tokens. <br>
Risk: The local MCP gateway could expose account operations if bound beyond localhost. <br>
Mitigation: Keep the gateway bound to 127.0.0.1 unless intentional exposure is reviewed and protected. <br>
Risk: The workflow can send email through Gmail after an approval path. <br>
Mitigation: Confirm that outbound email sending requires the expected approval flow and respects the UK business-hours scheduler before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asmaiqbal01/skills/deal-scout) <br>
- [Project repository](https://github.com/AsmaIqbal01/openclaw-deal-scout) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and tool descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes required Gmail, Gemini, and HubSpot environment variables, optional Discord notification settings, and local gateway host and port settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
