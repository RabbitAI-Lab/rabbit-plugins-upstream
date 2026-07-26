## Description: <br>
Comment @mason or @eureka in Linear issues to dispatch tasks to agents. Webhook receives Linear comments and routes to correct agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to route Linear issue comment mentions into Clawdbot agent sessions, providing issue context so agents can work on implementation, debugging, planning, or research tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Linear comments can trigger local agent workflows and may post back to Linear using configured write credentials. <br>
Mitigation: Use a dedicated least-privilege Linear bot token, require the webhook token, verify the webhook source, and route only issues approved for agent processing. <br>
Risk: Agent prompts and helper scripts include response-posting commands that read local credentials and use issue, agent, and response values. <br>
Mitigation: Remove the mandatory shell command from generated agent prompts, validate helper-script inputs, and prefer environment-managed secrets over local credential files. <br>
Risk: The transform includes an @forge route while the public documentation primarily describes @mason and @eureka. <br>
Mitigation: Confirm the allowed agent list before deployment and remove undocumented routes that should not receive Linear tasks. <br>


## Reference(s): <br>
- [Linear Webhooks API](https://developers.linear.app/docs/graphql/webhooks) <br>
- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/) <br>
- [Linear API Settings](https://linear.app/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with configuration examples, shell commands, and JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Linear issue context, agent routing metadata, and response-posting instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
