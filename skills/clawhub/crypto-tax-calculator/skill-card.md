## Description: <br>
Calculate crypto capital gains and losses using FIFO cost-basis accounting from a CSV of buy/sell transactions, with short-term and long-term summaries plus a Form 8949-style lot-by-lot CSV export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and crypto record keepers use this skill to process local transaction CSVs, estimate realized gains and losses, and prepare lot-level reports for review by a tax professional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Transaction CSVs may contain sensitive financial history. <br>
Mitigation: Process files locally, store inputs and exported reports intentionally, and avoid sharing them beyond trusted tax or accounting workflows. <br>
Risk: Incomplete buy history can cause sells without matching cost basis to be skipped. <br>
Mitigation: Provide complete transaction history for every asset and review any warnings before relying on the report. <br>
Risk: FIFO estimates may not match jurisdiction-specific tax treatment or filing requirements. <br>
Mitigation: Treat the output as preparation material and verify results with a qualified tax professional before filing. <br>


## Reference(s): <br>
- [Crypto Tax Calculator on ClawHub](https://clawhub.ai/ssidharhubble/skills/crypto-tax-calculator) <br>
- [README](README.md) <br>
- [Calculator script](scripts/tax_calc.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with bash command examples and a Python script that prints console summaries and can write CSV reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local CSV input with optional tax-year filtering and optional report output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
