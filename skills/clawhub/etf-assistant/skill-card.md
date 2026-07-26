## Description: <br>
ETF投资助理 / ETF Investment Assistant - 查询行情、筛选ETF、对比分析、定投计算。支持沪深300、创业板、科创50、纳指等主流ETF。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franky0617](https://clawhub.ai/user/franky0617) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External investors and agents use this skill to look up common ETF codes, retrieve Yahoo Finance quote data, search and compare ETFs, and estimate dollar-cost averaging outcomes. It is for reference workflows only and does not provide financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The calculator can run unintended shell commands if specially crafted numeric inputs are passed to it. <br>
Mitigation: Use only trusted, plain numeric amount and year inputs, and add numeric validation before exposing the script to untrusted input. <br>
Risk: ETF quote, comparison, and calculator outputs may be mistaken for investment advice. <br>
Mitigation: Treat the output as reference information only, preserve the documented investment-risk disclaimers, and verify decisions against authoritative financial sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/franky0617/skills/etf-assistant) <br>
- [Yahoo Finance chart endpoint used by the skill](https://query1.finance.yahoo.com/v8/finance/chart/510300.SS) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [CLI text output with ETF lists, quote summaries, comparisons, search results, and DCA estimates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Quote and comparison commands send ETF symbols to Yahoo Finance; calculator output depends on user-supplied numeric amount and year inputs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
