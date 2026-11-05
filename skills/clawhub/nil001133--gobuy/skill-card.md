## Description:

Assesses evidence for marketplace products and independent stores, analyzes review integrity, compares listings, and finds alternatives with stronger evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nil001133](https://clawhub.ai/user/nil001133)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents use GoBuy to assess product and storefront evidence, investigate review signals, and compare listings before advising a user. The results support a purchase decision but do not establish product quality or safety.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or store lookup targets may be received by the hosted service, and caller activity is pseudonymously tracked.

Mitigation: Limit lookups to information the user is comfortable sharing, and review the hosted service’s privacy terms before connecting the skill.

Risk: Evidence scores or heuristic review flags could be mistaken for proof of product quality, safety, or permission to purchase.

Mitigation: Describe scores as evidence quality, include verdict and freshness, qualify review findings as limited-sample heuristics, and follow the verification gate’s PASS, FLAG, or BLOCK outcome.

## Reference(s):

- [GPV-1 pre-purchase verification specification](https://docs.gobuy.ai/standard)
- [Universal Cart integration](https://docs.gobuy.ai/ucp)
- [Evidence Passport position paper](https://docs.gobuy.ai/passport)
- [MCP agent-channel statistics](https://mcp.gobuy.ai/stats)
- [GoBuy MCP registry listing](https://glama.ai/mcp/servers/gobuy-ai/gobuy-mcp)
- [Product evidence reports](https://audit.gobuy.ai)
- [Storefront audit](https://agentic.gobuy.ai)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Structured evidence results and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review forensics are on-demand and use a limited sample; findings are heuristic signals, not proof.]

## Skill Version(s):

2.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
