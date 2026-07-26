## Description: <br>
Create and manage scheduled bus arrival alerts using Korea TAGO OpenAPI and Clawdbot cron, including weekday or weekend rules that deliver arrival summaries through the user's configured Gateway messaging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hsooooo](https://clawhub.ai/user/hsooooo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and Clawdbot operators use this skill to register, test, list, and remove scheduled Korean metropolitan bus arrival alerts. It helps resolve TAGO stop and route inputs, build cron jobs, and produce short DM arrival summaries. <br>

### Deployment Geography for Use: <br>
South Korea <br>

## Known Risks and Mitigations: <br>
Risk: The setup helper can configure the Clawdbot Gateway environment and restart the user service. <br>
Mitigation: Use a dedicated TAGO API key where possible, review the selected Gateway systemd unit before applying changes, and keep the generated environment file private. <br>
Risk: The cron helper can list or remove Clawdbot cron jobs beyond this bus-alert workflow. <br>
Mitigation: Review cron job names and IDs before list or remove operations, and require explicit confirmation before deletion. <br>
Risk: DM-only delivery depends on the generated delivery target and is not fully enforced by the skill. <br>
Mitigation: Verify the channel and recipient target before registering a job, and run a one-time test before relying on recurring alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hsooooo/skills/korea-metropolitan-bus-alerts) <br>
- [TAGO API Reference](references/api_reference.md) <br>
- [Clawdbot Cron Recipe](references/cron_recipe.md) <br>
- [TAGO Bus Stop OpenAPI dataset](https://www.data.go.kr/data/15098534/openapi.do) <br>
- [TAGO Bus Arrival OpenAPI dataset](https://www.data.go.kr/data/15098530/openapi.do) <br>
- [Bus Stop Info API endpoint](https://apis.data.go.kr/1613000/BusSttnInfoInqireService) <br>
- [Bus Arrival Info API endpoint](https://apis.data.go.kr/1613000/ArvlInfoInqireService) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON cron job objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include TAGO lookup results, Korean arrival summaries, cron registration commands, and setup instructions; secrets should not be printed or embedded.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
