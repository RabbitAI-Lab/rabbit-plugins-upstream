## Description:

Read-only DeFi intelligence for opportunity research, portfolio diagnostics, allocation analysis, route previews, Trail Heat, and Sybil review. Never executes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External DeFi users and agents use this skill to research protocols, airdrops, points programs, public-wallet diagnostics, route previews, and Sybil-risk signals. It provides analysis and guidance only, without signing or executing transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public wallet addresses and research parameters may be sent to FarmDash for read-only DeFi analysis.

Mitigation: Use the skill only with public wallet and research inputs you are comfortable sending to FarmDash; do not provide private keys, seed phrases, wallet exports, OAuth tokens, signed messages, or transactions.

Risk: Actionable DeFi recommendations may include disclosed FarmDash affiliate or routing links.

Mitigation: Independently verify protocol destinations and commercial disclosures before moving funds, and treat routes as optional rather than execution instructions.

Risk: DeFi analysis, Trail Heat scores, and Sybil heuristics can be incomplete, stale, or speculative.

Mitigation: Use the output as research guidance only, confirm protocol terms and data quality, and make any transaction through a separate user-controlled execution path.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash Trail Intelligence ClawHub Listing](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-intelligence)
- [FarmDash MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with structured DeFi analysis and disclosed links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; no transaction signing, execution, or wallet write actions.]

## Skill Version(s):

1.0.19 (source: ClawHub server release evidence; artifact frontmatter reports 3.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
