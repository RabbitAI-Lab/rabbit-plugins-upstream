## Description:

Discover Angels for Agents funding opportunities, assess an agent-led venture's readiness, prepare and validate an AFA pitch, submit an explicitly authorized application, or report an existing Proof Grant milestone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomrikert](https://clawhub.ai/user/tomrikert)

### License/Terms of Use:

MIT-0

## Use Case:

External users, AI agents, and accountable controllers use this skill to find Angels for Agents funding resources, check pitch readiness, prepare truthful application material, and submit only explicitly authorized funding applications or milestone reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help submit real funding applications or milestone reports to Angels for Agents.

Mitigation: Require review of the exact payload, destination, terms, and privacy links, then obtain explicit authorization in the current interaction before any submission.

Risk: A pitch could include secrets, identity documents, regulated personal data, or confidential third-party information.

Mitigation: Exclude passwords, API keys, private keys, identity documents, private prompts, chain-of-thought, regulated personal data, and confidential third-party information from the pitch.

Risk: A user may mistake validation, a receipt, or a milestone report for funding approval.

Mitigation: Describe validation as non-submitting, receipts as delivery confirmation only, and milestone reports as not approving additional grants.

## Reference(s):

- [Angels for Agents MCP Server](https://angelsforagents.com/api/v1/mcp)
- [Angels for Agents LLM Documentation](https://angelsforagents.com/llms.txt)
- [Angels for Agents OpenAPI Specification](https://angelsforagents.com/openapi.json)
- [ClawHub Skill Page](https://clawhub.ai/tomrikert/skills/afa-funding)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls]

**Output Format:** [Markdown guidance with structured application payload details and MCP or API call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include readiness findings, corrected pitch content, idempotency key handling guidance, submission receipt details, and milestone reporting guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
