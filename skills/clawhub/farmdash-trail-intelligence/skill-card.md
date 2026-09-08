## Description:

Use when researching DeFi protocols: Trail Heat scores, sybil risk, yield and points simulation. Read-only; never signs, approves, or executes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External DeFi researchers and agents use this skill to compare protocols, inspect Trail Heat and Sybil-risk signals, simulate points scenarios, and prepare read-only capital-allocation research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FarmDash-hosted DeFi analytics may receive public wallet and route-planning details.

Mitigation: Use only public wallet data, avoid submitting secrets or signatures, and install only if this data sharing is acceptable.

Risk: Recommendations may include FarmDash affiliate routes or paid-tier prompts.

Mitigation: Treat routes as optional, verify canonical protocol destinations and fees independently, and do not rely on affiliation as a quality signal.

Risk: Personalized DeFi capital guidance can be speculative or misleading if treated as execution advice.

Mitigation: Treat outputs as research, review risk notes and data-quality caveats, and make any transaction decision outside this read-only skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-intelligence)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)
- [FarmDash Fee Structure](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown or structured text with DeFi research summaries, risk notes, and optional tool-call results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; may include affiliate-route disclosures, paid-tier prompts, and data-quality caveats.]

## Skill Version(s):

1.0.18 (source: server release metadata; artifact frontmatter reports 3.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
