## Description: <br>
Query Topical topic intelligence via MCP: breaking news, signals, trends, and source links from scheduled runs for topic briefings, competitive intel, and monitoring updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daveangelcode](https://clawhub.ai/user/daveangelcode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams with Topical accounts use this skill to retrieve scheduled topic intelligence, source-linked narratives, and monitoring updates. It can also guide account-scoped actions such as feedback, source subscriptions, schedules, and agent webhook settings through Topical MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP setup uses a long-lived Topical Agent API key. <br>
Mitigation: Store the key only in the MCP server configuration, restrict access to local OpenClaw configuration, and rotate it if it is exposed. <br>
Risk: Persistent Topical webhooks can wake the agent and relay external news content. <br>
Mitigation: Review the hook mapping before enabling it, test with delivery disabled when appropriate, and require a hook bearer token plus Topical signature verification. <br>
Risk: Some MCP tools can change the account's monitored sources, topic schedule, feedback signals, or agent webhook configuration. <br>
Mitigation: Treat those tools as account-changing actions and invoke them only when the user has clearly requested the change. <br>


## Reference(s): <br>
- [Topical website](https://usetopical.com) <br>
- [Topical OpenClaw portal](https://app.usetopical.com/portal/openclaw/) <br>
- [ClawHub Topical skill](https://clawhub.ai/daveangelcode/skills/topical) <br>
- [ClawHub Topical OpenClaw setup skill](https://clawhub.ai/daveangelcode/skills/topical-openclaw-setup) <br>
- [Topical agent webhook payloads](references/payloads.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples; MCP responses may include structured JSON payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs reflect the authenticated account's latest completed Topical pipeline run or requested checkpoint, not live web search.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
