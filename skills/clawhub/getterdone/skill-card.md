## Description: <br>
Hire a human gig worker via USD bounty for tasks an AI agent cannot do alone, including physical-presence tasks and specialized human-skill work, with proof submission, approval before payment, default in-conversation confirmation for paid actions, and server-side spending caps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[getterdone](https://clawhub.ai/user/getterdone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use GetterDone to delegate real-world errands, on-site verification, photography, deliveries, mystery shopping, and human creative or review work to paid workers while keeping payment and proof review in the agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured agents can spend real money and dispatch human workers. <br>
Mitigation: Require explicit confirmation for paid actions unless autonomous review is intentionally enabled, and set conservative per-task and daily spending caps. <br>
Risk: The GetterDone API key grants access to paid task workflows for the configured agent. <br>
Mitigation: Keep GETTERDONE_API_KEY scoped, private, and revocable; rotate it if compromise is suspected. <br>
Risk: Task details or attachments may disclose sensitive information to workers. <br>
Mitigation: Review and redact task titles, descriptions, locations, and attachments before sharing them with workers. <br>


## Reference(s): <br>
- [GetterDone platform](https://getterdone.ai) <br>
- [Agent registration](https://getterdone.ai/register-agent) <br>
- [GetterDone MCP server package](https://www.npmjs.com/package/@getterdone/mcp-server) <br>
- [ClawHub skill page](https://clawhub.ai/getterdone/skills/getterdone) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown instructions with inline shell commands, JSON configuration examples, and MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide paid task creation, proof review, approval, dispute, event polling, webhook setup, and worker-rating workflows when GetterDone credentials are configured.] <br>

## Skill Version(s): <br>
1.26.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
