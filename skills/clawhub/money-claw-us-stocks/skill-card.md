## Description:

Screens and ranks U.S.-listed common stocks, ordinary shares, and ADR/ADS securities for extreme low-float squeeze moves by checking point-in-time prices, liquidity, share supply, premarket and official-open gaps, turnover, spreads, VWAP, catalysts, splits, dilution, halts, and data quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qinjobs](https://clawhub.ai/user/qinjobs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert U.S. premarket movers and intraday low-float stocks into standardized quantitative states, watchlists, risk checks, and batch scoring outputs. It is trading research software and does not provide personalized investment advice or place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs can be mistaken for investment advice or direct trading instructions.

Mitigation: Present EXECUTE and related labels as research gate states only; users must make independent suitability, risk, and trading decisions.

Risk: Low-float and halted stocks can have stale quotes, wide spreads, slippage, disappearing liquidity, or halt gaps that exceed planned stops.

Mitigation: Independently verify live quotes, spread, halt status, VWAP, turnover, and position sizing before relying on any output.

Risk: Share-supply events such as ATM programs, offerings, resale registrations, warrants, convertibles, PIPEs, or unlocks can invalidate a squeeze setup.

Mitigation: Verify SEC filings, issuer announcements, and exchange information; confirmed supply risk should force EXCLUDE and unresolved supply checks should remain WAIT_DATA.

Risk: Connecting the workflow to broker execution could create security, compliance, and financial harm beyond the skill's disclosed behavior.

Mitigation: Do not connect it to live order routing without a separate security, compliance, and legal review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qinjobs/skills/money-claw-us-stocks)
- [Publisher profile](https://clawhub.ai/user/qinjobs)
- [Factor model](references/factor-model.md)
- [2026 extreme-move case studies](references/case-studies-2026.md)
- [500% extreme-move intraday playbook](references/intraday-500pct-playbook.md)
- [CYCU 5-minute case study](references/cycu-2026-07-30.md)
- [CYCU investor-relations release](https://investors.cycurion.com/pr/cycurion-lands-largest-contract-in-company-history-546-million-10year-award-with-top5-global-consulting-firm)
- [SEC filing: CYCU Form S-1](https://www.sec.gov/Archives/edgar/data/1868419/000149315226031976/forms-1.htm)
- [SEC filing: CYCU 2026 filing](https://www.sec.gov/Archives/edgar/data/1868419/000162828026048496/cycu-20260710.htm)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown analysis with optional JSON and command-line scoring outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces model-state labels such as EXECUTE, WAIT_OPEN, WAIT_DATA, WATCH, and EXCLUDE; outputs are research gates, not broker orders.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
