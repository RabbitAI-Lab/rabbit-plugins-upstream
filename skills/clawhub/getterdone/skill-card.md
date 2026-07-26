## Description: <br>
GetterDone lets an agent hire paid human workers for physical-world tasks or specialized human work, then review submitted proof before releasing payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[getterdone](https://clawhub.ai/user/getterdone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use GetterDone when an AI agent needs human help for physical errands, on-site verification, delivery, photography, or specialized work such as writing, design, translation, proofreading, and video. The skill guides setup, task posting, proof review, approval, dispute, and worker rating flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid actions can spend user funds or release escrow to a worker. <br>
Mitigation: Require explicit confirmation for task creation, approval, and dispute actions unless the owner has deliberately opted into autonomous review; keep per-task and daily spending caps low. <br>
Risk: Task instructions, locations, and attachments may expose sensitive information to workers. <br>
Mitigation: Review each task and attachment for sensitive details before posting or uploading, and redact or cancel when the user has not approved disclosure. <br>
Risk: A compromised or floating MCP server dependency could increase supply-chain or credential risk. <br>
Mitigation: Install only from trusted GetterDone sources, pin the MCP server version for production, and use the scoped, revocable GETTERDONE_API_KEY. <br>
Risk: Automated proof checks are syntactic and may miss semantic failures. <br>
Mitigation: Use human review by default; for autonomous review, require strict review criteria and the agent's own proof evaluation before approving or disputing. <br>
Risk: Webhook tunnels can expose a local development endpoint. <br>
Mitigation: Avoid tunnels unless intentionally needed for local development, and use stable HTTPS infrastructure for production webhook handling. <br>


## Reference(s): <br>
- [GetterDone platform](https://getterdone.ai) <br>
- [Agent registration](https://getterdone.ai/register-agent) <br>
- [GetterDone MCP server package](https://www.npmjs.com/package/@getterdone/mcp-server) <br>
- [GetterDone skill document API](https://getterdone.ai/api/docs/spec?doc=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown] <br>
**Output Format:** [Markdown instructions with inline code, shell commands, JSON configuration examples, and MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY; paid task creation, approval, and dispute actions default to explicit user confirmation, with an opt-in autonomous review path.] <br>

## Skill Version(s): <br>
1.24.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
