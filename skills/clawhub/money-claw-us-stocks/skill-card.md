## Description:

Screens and ranks U.S.-listed common stocks, ordinary shares, and ADR/ADS securities for extreme low-float squeeze moves by checking point-in-time price action, liquidity, share supply, issuer news, SEC filings, halts, splits, dilution, and data quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qinjobs](https://clawhub.ai/user/qinjobs)

### License/Terms of Use:

MIT-0

## Use Case:

External investors and traders, especially Asia-Pacific users monitoring U.S. sessions, use this skill to convert premarket, regular-session, and after-hours micro-cap movers into auditable candidate rankings, watch states, and risk checklists. It supports research workflow outputs and batch CSV/JSON scoring, but its model states are not personalized investment advice or automatic trading instructions.

### Deployment Geography for Use:

Global, with primary trading timestamps in U.S. Eastern Time and optional secondary local-time references for Asia-Pacific users.

## Known Risks and Mitigations:

Risk: The skill analyzes volatile low-float stocks and can produce trading-state labels or position-sizing examples that may be mistaken for personalized trading advice.

Mitigation: Treat outputs as research workflow states only; independently verify issuer news, SEC filings, liquidity, suitability, and local regulatory obligations before any real trade.

Risk: Market data, share counts, float, corporate actions, and news can be delayed, incomplete, or inconsistent during fast premarket, regular-session, and after-hours moves.

Mitigation: Use timestamped point-in-time sources, preserve UNKNOWN for missing fields, and confirm material data through brokers, exchanges, regulators, issuer pages, and SEC filings.

Risk: Extreme micro-cap moves can halt, gap through stops, become illiquid, or expose users to dilution and supply overhang risk.

Mitigation: Block EXECUTE when supply risk is confirmed, avoid stale halt quotes and market-order chasing, and revalidate VWAP, spread, turnover, and first-five-minute structure after resumption or the next session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qinjobs/skills/money-claw-us-stocks)
- [Factor model reference](references/factor-model.md)
- [2026 case studies](references/case-studies-2026.md)
- [500% extreme-move intraday playbook](references/intraday-500pct-playbook.md)
- [CYCU 2026-07-30 case study](references/cycu-2026-07-30.md)
- [CYCU company press release](https://investors.cycurion.com/pr/cycurion-lands-largest-contract-in-company-history-546-million-10year-award-with-top5-global-consulting-firm)
- [CYCU SEC S-1](https://www.sec.gov/Archives/edgar/data/1868419/000149315226031976/forms-1.htm)
- [CYCU SEC Form 8-K](https://www.sec.gov/Archives/edgar/data/1868419/000162828026048496/cycu-20260710.htm)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown briefs and checklists, plus optional JSON or Markdown batch-scoring output from Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit model states such as EXECUTE, WAIT_OPEN, WAIT_DATA, WATCH, and EXCLUDE; evidence scores are rankings, not probability forecasts.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
