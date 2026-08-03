## Description: <br>
Connect OpenClaw to IFTTT's hosted MCP server to discover triggers and actions, build and manage Applets, and run actions and queries across connected services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ifttt](https://clawhub.ai/user/ifttt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to connect an agent to IFTTT, discover supported services, create or manage Applets, and run approved actions or queries on connected services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create enabled automations or run one-off actions that affect connected services such as email, lights, spreadsheets, or webhooks. <br>
Mitigation: Review the proposed trigger, actions, connected accounts, and side effects before approving Applet creation, deletion, or direct action execution. <br>
Risk: IFTTT service or account authorization can be missing or expired, causing automation requests to fail until the user reconnects the service. <br>
Mitigation: Use IFTTT-provided connect or reconnect URLs, wait for user confirmation, and retry only after authorization is complete. <br>
Risk: Some IFTTT capabilities are plan gated, including Filter Code for Pro+ accounts. <br>
Mitigation: Check the user's plan before attempting gated operations and explain the required plan when a restriction applies. <br>


## Reference(s): <br>
- [IFTTT plugin source homepage](https://github.com/IFTTT/ifttt-plugins) <br>
- [IFTTT](https://ifttt.com) <br>
- [IFTTT MCP server](https://ifttt.com/mcp) <br>
- [IFTTT plans](https://ifttt.com/plans) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OAuth setup guidance, service connection URLs, Applet summaries, and confirmation prompts before real-world actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
