## Description:

Screens U.S. premarket and after-hours low-float, low-priced stock movers for extreme-squeeze candidates while checking catalysts, share supply, liquidity, VWAP, halts, dilution, and data quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qinjobs](https://clawhub.ai/user/qinjobs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn U.S. premarket and after-hours movers, screenshots, or candidate CSV/JSON files into ranked research states, validation checklists, and risk controls. It supports screening and workflow standardization, not personalized investment advice or automated trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat screening states or ranked candidates as trading instructions.

Mitigation: Present outputs as research aids and independently verify market data, filings, liquidity, and legal suitability before making any financial decision.

Risk: Low-priced, low-float, or halted stocks can move sharply with poor liquidity, slippage, or gap risk.

Mitigation: Use the skill's risk controls, avoid market orders around premarket moves or halt resumptions, and recheck spread, VWAP, turnover, halt, and split conditions before acting.

Risk: Incomplete or stale market data can distort gap, float, turnover, VWAP, or dilution checks.

Mitigation: Mark missing fields as UNKNOWN or WAIT_DATA and verify point-in-time prices, share counts, corporate actions, news, and filings through primary sources.

Risk: Unresolved share-supply overhang can invalidate an extreme-move candidate.

Mitigation: Check SEC and issuer disclosures for active ATM programs, registered resale, warrants, PIPE, equity-line, convertibles, lock-up releases, and offerings; exclude candidates when current supply risk is confirmed.

## Reference(s):

- [Money Claw ClawHub Skill Page](https://clawhub.ai/qinjobs/skills/money-claw-us-stocks)
- [README_EN.md](README_EN.md)
- [Factor Model](references/factor-model.md)
- [500% Extreme-Move Intraday Playbook](references/intraday-500pct-playbook.md)
- [2026 Extreme-Move Case Methodology](references/case-studies-2026.md)
- [CYCU 5-Minute Case Study - 2026-07-30](references/cycu-2026-07-30.md)
- [CYCU Company Press Release](https://investors.cycurion.com/pr/cycurion-lands-largest-contract-in-company-history-546-million-10year-award-with-top5-global-consulting-firm)
- [CYCU SEC Form S-1 Filing](https://www.sec.gov/Archives/edgar/data/1868419/000149315226031976/forms-1.htm)
- [CYCU SEC Filing - 2026-07-10](https://www.sec.gov/Archives/edgar/data/1868419/000162828026048496/cycu-20260710.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown narratives, checklists, tables, and optional JSON batch-scoring results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model states such as EXECUTE, WAIT_OPEN, WAIT_DATA, WATCH, and EXCLUDE; these are research workflow states, not trading orders.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
