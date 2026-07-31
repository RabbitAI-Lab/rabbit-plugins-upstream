## Description: <br>
把中国3C新品营销从“想创意”推进到“能执行、早避雷、能复盘”的策略技能包。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Marketing, product, social content, KOL/channel, and startup teams use this skill to plan China 3C product launches, review messaging and formal materials, generate campaign ideas, evaluate competitor threats, detect negative signals, and structure post-launch reviews. It is intended for marketing decision support, not personal shopping, repair troubleshooting, legal approval, advertising compliance approval, or product-safety signoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-timeliness marketing facts such as prices, rankings, market share, new product specifications, platform heat, and recent KOL reputation may be stale or unavailable in the packaged knowledge base. <br>
Mitigation: Verify current facts before using them in formal outputs, and mark unresolved claims as [待验证] or 知识库暂无此数据. <br>
Risk: Launch go/no-go recommendations may be mistaken for legal, advertising-compliance, product-safety, or brand approval. <br>
Mitigation: Use the skill as marketing decision support only, and route final decisions through the relevant approval owners. <br>
Risk: Data-import workflows may propose updates to knowledge-base indexes or SKILL.md. <br>
Mitigation: Review diffs before accepting imported-data updates and keep those workflows scoped to intended marketing evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/killsnake01/skills/china-marketing-copilot) <br>
- [Agent Router](docs/agent-router.md) <br>
- [Data Index and Freshness Rules](docs/data-index.md) <br>
- [Runtime Capabilities](docs/runtime-capabilities.json) <br>
- [Data Sources Freshness Ledger](docs/data-sources.json) <br>
- [Evidence Ledger](docs/evidence-ledger.json) <br>
- [Launch Decision Card](assets/launch-decision-card.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown, structured tables, JSON where requested, and occasional shell commands for bundled validation scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include evidence labels, freshness markers, confidence self-checks, launch decisions, route scorecards, risk ledgers, KOL/channel briefs, material reviews, and post-launch review structures.] <br>

## Skill Version(s): <br>
1.4.33 (source: release evidence and VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
