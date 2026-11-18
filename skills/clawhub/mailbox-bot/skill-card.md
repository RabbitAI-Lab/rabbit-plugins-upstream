## Description:

Postal mail API and MCP server for AI agents: send letters, certified mail and postcards, and give an agent its own street address + PMB with webhooks, OCR search and human-approved scan, forward or discard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arbengine](https://clawhub.ai/user/arbengine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use mailbox.bot to send physical letters and batch mail, work with forwarded mail context, and search agent mailbox mail. Agents can propose inbound mail actions for a person to approve.

### Deployment Geography for Use:

United States (the documented postal and agent mailbox services are US-based)

## Known Risks and Mitigations:

Risk: The security review flags an unpinned installation command and a mismatch between the skill's mailbox purpose and its package publishing workflow; the scan is partial.

Mitigation: Follow the security guidance: defer installation until the publisher clarifies the publishing instructions and provides pinned, reviewable install versions.

Risk: Live mail actions can incur charges, and inbound mail handling can include forwarding or discard proposals.

Mitigation: Use sandbox keys and dry runs to review costs; require the account owner's approval for proposed inbound actions and review outbound mail before sending.

Risk: API keys and webhook credentials can expose account access if copied into prompts, URLs, or logs.

Mitigation: Keep credentials in protected configuration and out of URLs, copied prompts, and logs.

## Reference(s):

- [API documentation](https://mailbox.bot/api-docs)
- [MCP installation guide](https://mailbox.bot/mcp-install)
- [OpenAPI specification](https://mailbox.bot/openapi.json)
- [Public MCP tool catalog](https://mailbox.bot/api/mcp/tools-public)
- [Pricing](https://mailbox.bot/pricing)
- [Sandbox documentation](https://mailbox.bot/api-docs#sandbox)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTTP, shell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may contain placeholders for API keys, addresses, and mail documents.]

## Skill Version(s):

5.3.3 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
