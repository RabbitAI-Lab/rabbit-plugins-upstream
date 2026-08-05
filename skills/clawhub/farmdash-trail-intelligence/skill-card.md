## Description: <br>
Research and rank DeFi protocols, airdrops, points programs, Trail Heat, FarmScore inputs, sybil-policy risk, and live protocol events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to research DeFi protocols, airdrop and points opportunities, wallet health, route feasibility, and protocol events. It supports read-only analysis and planning, not transaction execution or custody. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send public wallet addresses, token details, chain IDs, and portfolio-sizing inputs to FarmDash services. <br>
Mitigation: Use only public wallet data, review what will be sent before tool use, and avoid sending private keys, seed phrases, signatures, wallet exports, OAuth tokens, or write permissions. <br>
Risk: DeFi recommendations and route feasibility output can be mistaken for financial advice or automatic trading instructions. <br>
Mitigation: Treat output as research only, require explicit user decisions for any state-changing action, and use a separate execution path for signing or transactions. <br>
Risk: Affiliate or referral routes may influence user perception of recommendations. <br>
Mitigation: Disclose FarmDash compensation when a FarmDash route is shown, keep safety warnings referral-free, and avoid showing managed routes for avoid or high-risk verdicts. <br>
Risk: Sybil-risk and points simulations are heuristic and may be misused to evade protocol anti-abuse controls. <br>
Mitigation: Use the results for risk awareness and compliance planning only; do not provide timing, wallet-creation, or activity-shaping steps intended to bypass protocol policies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-intelligence) <br>
- [FarmDash Agent Hub](https://www.farmdash.one/agents) <br>
- [FarmDash MCP Configuration](https://www.farmdash.one/.well-known/mcp.json) <br>
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml) <br>
- [FarmDash Fee Structure](https://www.farmdash.one/fees) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown with structured analysis, risk notes, disclosures, and optional setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only DeFi research output; may include public wallet analysis, tier limits, timestamps, source attribution, and affiliate-route disclosures.] <br>

## Skill Version(s): <br>
1.0.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
