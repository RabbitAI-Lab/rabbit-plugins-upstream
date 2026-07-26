## Description: <br>
mailbox.bot is a remote MCP server that lets AI agents send outbound physical mail, use forwarded inbound document context, retrieve source documents, manage linked postal threads, and test workflows in sandbox before live use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arbengine](https://clawhub.ai/user/arbengine) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external agent builders use this skill to connect agents to mailbox.bot's postal-mail workflows for outbound print-and-mail, inbound forwarded document context, linked replies, source-document review, and sandbox testing before real sends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The integration can send physical mail and may incur real-world costs or trigger fulfillment workflows. <br>
Mitigation: Use sandbox or dry_run first, prefer agent-scoped test keys, set cost caps, and require human approval for real sends. <br>
Risk: The integration can read inbound mail context and source documents that may contain sensitive information. <br>
Mitigation: Use scoped agent keys, limit document.read access to agents that need it, and review source-document retrieval before enabling production access. <br>
Risk: Automatic mail rules may permanently shred, dispose of, or discard physical mail. <br>
Mitigation: Do not allow automatic shred, dispose, or discard rules unless the sender or category is tightly defined and a human has approved the policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arbengine/skills/mailbox-bot) <br>
- [mailbox.bot homepage](https://mailbox.bot) <br>
- [MCP install guide](https://mailbox.bot/mcp-install) <br>
- [API documentation](https://mailbox.bot/api-docs) <br>
- [OpenAPI specification](https://mailbox.bot/openapi.json) <br>
- [Public MCP tool catalog](https://mailbox.bot/api/mcp/tools-public) <br>
- [Sandbox documentation](https://mailbox.bot/api-docs#sandbox) <br>
- [Pricing](https://mailbox.bot/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration and shell/API command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP configuration, REST examples, approval guidance, sandbox/dry-run instructions, and cost-control recommendations.] <br>

## Skill Version(s): <br>
5.1.6 (source: server evidence, frontmatter, changelog released 2026-07-08, server.json, smithery.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
