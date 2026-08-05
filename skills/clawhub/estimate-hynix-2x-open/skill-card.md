## Description: <br>
Estimates timestamped NAV fair value and tradable-price scenarios for HKEX 07709 using verified NAV, KRX 000660, Nasdaq SKHY, ADS ratio, FX, and prior discount inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qinjobs](https://clawhub.ai/user/qinjobs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate HKEX 07709 fair opening or intraday value, compare NAV fair value with tradable-price scenarios, and surface market-data and leverage-product risks before acting on a valuation estimate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The estimate may be mistaken for a guaranteed executable price or financial advice. <br>
Mitigation: Present outputs as timestamped estimates, include a scenario range, and state that users must independently verify market data and product filings before making decisions. <br>
Risk: Stale or incorrect NAV, KRX, SKHY, FX, or ADS-ratio inputs can materially distort the valuation. <br>
Mitigation: Require timestamped inputs, verify symbols and ADS ratio from current primary sources, and label stale or unavailable data explicitly. <br>
Risk: Leverage reset, tracking error, derivative capacity, market-maker inventory, and bid-ask spreads can keep the market price away from NAV. <br>
Mitigation: Report NAV fair value separately from carried premium or discount scenarios and include warnings for large secondary-market deviations. <br>
Risk: KRX suspensions, delayed quotes, circuit breakers, or large intraday moves can invalidate a single point estimate. <br>
Mitigation: Prefer the latest reliable KRX quote when available and recalculate opening, latest, and scenario values when underlying moves are extreme. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qinjobs/skills/estimate-hynix-2x-open) <br>
- [Methodology and sources](references/methodology.md) <br>
- [HKEX product document](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0622/2026062200892.pdf) <br>
- [CSOP product page](https://www.csopasset.com/en/products/hk-skhy-2l) <br>
- [SEC ADS ratio filing](https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm) <br>
- [Citi depositary receipts directory](https://depositaryreceipts.citi.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with valuation tables, warnings, and optional inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires externally supplied timestamped market data; the bundled calculator performs deterministic local calculations and does not fetch quotes, store credentials, or trade.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
