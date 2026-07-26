## Description: <br>
Scalekit Agent Auth helps OpenClaw agents discover, authorize, and execute tools for connected third-party services through Scalekit Connect, with proxy fallback when catalog tools are unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avinash-kamath](https://clawhub.ai/user/avinash-kamath) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to let OpenClaw agents work with connected SaaS tools such as Notion, Slack, Gmail, GitHub, HubSpot, and Google Sheets. It guides the agent through connection discovery, authorization checks, tool schema lookup, execution, and proxy fallback when a catalog tool is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad access to services connected through Scalekit. <br>
Mitigation: Use least-privilege Scalekit credentials, connect only the providers needed for the deployment, and require explicit user approval before sends, deletes, file transfers, proxy requests, or other mutating actions. <br>
Risk: The available CLI includes a command that can reveal raw OAuth access and refresh tokens. <br>
Mitigation: Do not use the token-inspection command in agent workflows, avoid logging command output, and restrict token inspection to controlled manual debugging. <br>
Risk: Proxy fallback can make direct provider API requests when no catalog tool covers the requested action. <br>
Mitigation: Use proxy fallback only after tool discovery confirms no suitable catalog tool exists, and review the method, path, headers, body, files, and query parameters before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/avinash-kamath/skills/scalekit-agent-auth) <br>
- [Publisher profile](https://clawhub.ai/user/avinash-kamath) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Scalekit](https://scalekit.com) <br>
- [Scalekit Notion connector setup guide](https://docs.scalekit.com/reference/agent-connectors/notion/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON tool inputs or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authorization links, connected-service results, proxy request guidance, or file transfer instructions depending on the requested provider action.] <br>

## Skill Version(s): <br>
2.4.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
