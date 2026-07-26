## Description: <br>
Minimax Monitor launches a local MiniMax quota dashboard for token-plan usage, model limits, 24-hour trends, and opt-in inference latency testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjipeng977](https://clawhub.ai/user/wangjipeng977) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and MiniMax users use this skill to open a local dashboard that checks remaining MiniMax Token Plan quota, tracks recent usage, and optionally runs latency probes after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that opening the dashboard may automatically use the local MiniMax API key from ~/.mmx/config.json and contact MiniMax. <br>
Mitigation: Review the skill before installing, run it only on a trusted local machine, and ensure you are comfortable with local API-key use before opening the dashboard. <br>
Risk: The skill starts a localhost service on port 9877. <br>
Mitigation: Keep the service bound to local interfaces, do not expose port 9877 to other networks, and stop the server when the dashboard is no longer needed. <br>
Risk: Quota polling sends outbound requests to MiniMax and the optional speed test can consume tokens. <br>
Mitigation: Expect outbound polling while the dashboard is running, stop the server when monitoring is not needed, and use the latency probe only after confirming the token cost. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangjipeng977/skills/minimax-monitor) <br>
- [Metadata source: MiniMax-AI skills](https://github.com/MiniMax-AI/skills) <br>
- [MiniMax token plan API endpoint](https://www.minimaxi.com/v1/token_plan/remains) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and local dashboard guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Starts a localhost dashboard on port 9877, polls MiniMax quota data, and may write a local history.jsonl usage trend file.] <br>

## Skill Version(s): <br>
1.7.0 (source: server evidence release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
