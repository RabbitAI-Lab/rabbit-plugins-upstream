## Description: <br>
Hua Personal Strategy helps an agent use HuahuaDaily portfolio data, user investment policy, external research evidence, and deterministic calculation scripts to produce auditable mutual-fund hold, buy, sell, rebalance, or cash-waiting drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baiye1997](https://clawhub.ai/user/baiye1997) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users who connect HuahuaDaily portfolio data use this skill to create and maintain an investment policy, research mutual-fund holdings, and generate auditable hold, buy, sell, rebalance, or cash-waiting drafts. It is not for automatic trading, stock or exchange-traded ETF execution, public fund recommendations without authorized holdings, or promises of investment accuracy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive portfolio data and persists local investment-policy and activity history. <br>
Mitigation: Install it only for intended HuahuaDaily portfolio workflows, confirm archival settings before use, and restrict access to the local state directory. <br>
Risk: Generated investment drafts could be mistaken for executed trades or guaranteed outcomes. <br>
Mitigation: Keep real trades in the app confirmation flow and review proposed amounts, blockers, evidence, and audit hashes before acting. <br>
Risk: Security evidence flags unclear archival and permission boundaries. <br>
Mitigation: Review snapshot, archival, and local-state behavior before deployment, and avoid implicit or background use for unrelated finance requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baiye1997/skills/hua-personal-strategy) <br>
- [Policy Contract](references/policy-contract.md) <br>
- [Runtime Protocol](references/runtime-protocol.md) <br>
- [Decision Contract](references/decision-contract.md) <br>
- [Action Model](references/action-model.md) <br>
- [Factor Model](references/factor-model.md) <br>
- [AI Output Governance](references/ai-output-governance.json) <br>
- [Report Contract](references/report-contract.md) <br>
- [Evolution Protocol](references/evolution-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese natural-language recommendations, JSON audit artifacts, and optional self-contained HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Trading amounts are proposals from deterministic scripts and still require user confirmation in the app.] <br>

## Skill Version(s): <br>
4.3.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
