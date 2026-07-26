## Description: <br>
HuaHuaDailyMCP lets agents use authorized HuahuaDaily MCP tools for portfolio and transaction queries, fund and market data, strategy backtests, quant snapshots, community actions, screenshot recognition, and App-confirmed trade or import requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baiye1997](https://clawhub.ai/user/baiye1997) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External HuahuaDaily users and their agents use this skill to inspect authorized portfolio data, analyze funds and markets, run portfolio backtests, prepare quant snapshots, use community features, and submit trade or import requests that require App confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive financial data through the user's HuahuaDaily Agent Token. <br>
Mitigation: Install only if the publisher is trusted, use the narrowest available token scopes, and revoke the token when access is no longer needed. <br>
Risk: Screenshot recognition can upload user-provided screenshot paths for processing. <br>
Mitigation: Provide screenshot paths only when the user intends those images to be uploaded for recognition. <br>
Risk: Some community and report actions can directly affect the user's HuahuaDaily account. <br>
Mitigation: Review direct community and report actions before allowing the agent to call them. <br>
Risk: Trade and import requests involve financial workflows. <br>
Mitigation: Use the skill's App-confirmed flow: agent requests create pending actions, while final trade or import confirmation remains in the HuahuaDaily App. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baiye1997/skills/huahua-daily) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style MCP tool call arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sensitive financial data from authorized HuahuaDaily accounts; trade and import requests remain pending until App confirmation.] <br>

## Skill Version(s): <br>
2.8.1 (source: server release metadata; artifact frontmatter/runtime report 2.8.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
