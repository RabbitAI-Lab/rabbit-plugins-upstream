## Description:

Run an assisted customer research business through a dedicated Mermail inbox, from requirements clarification and owner-verified orders to sourced protocol comparisons, crypto market reports, approved delivery, and same-thread follow-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace owners use this skill to operate an assisted customer research inbox for owner-verified protocol comparisons, crypto market reports, approved email delivery, and same-thread follow-ups using Mermail and available CMC research capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare external email replies and paid data purchase requests in a customer research workflow.

Mitigation: Require owner authorization for the exact recipients, report content, rights, and purchase terms before any send or paid data access.

Risk: Mermail workspace and mailbox access depends on the provided API key, and PayBox access may be connected separately by the owner.

Mitigation: Install only in trusted Mermail workspaces, protect the API key, and confirm any PayBox connection before using wallet-enabled operations.

Risk: Customer messages, attachments, provider output, and payment challenges may contain untrusted instructions or unsupported claims.

Mitigation: Treat those inputs as data, keep work within the owner-verified order scope, verify source-use rights, and hold delivery when entitlement, rights, or evidence is missing.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Research Agent on ClawHub](https://clawhub.ai/mermail/skills/mermail-research-agent)
- [CMC Research and Additional Data](references/cmc-research.md)
- [Research Business Security](references/security.md)
- [Research Engagement Workflow](references/workflows.md)
- [Research Agent Tool Contracts](references/tools.md)
- [Order and Report Templates](references/templates.md)
- [Official Crypto Research Workflow](https://pro.coinmarketcap.com/api/documentation/ai-agent-hub/skills/crypto-research)
- [Official Market Report Workflow](https://pro.coinmarketcap.com/api/documentation/ai-agent-hub/skills/market-report)
- [CMC MCP](https://pro.coinmarketcap.com/api/documentation/ai-agent-hub/mcp)
- [CMC x402 Endpoints and Protocol](https://pro.coinmarketcap.com/api/documentation/ai-agent-hub/x402)
- [Mermail MCP Endpoint](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown and structured status text for drafts, sourced memos, private owner checkpoints, clarification requests, and purchase proposals.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained by owner authorization, verified order scope, rights checks, recipient review, and available Mermail, CMC, and PayBox capabilities.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
