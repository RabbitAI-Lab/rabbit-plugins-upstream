## Description: <br>
Detects unusual options activity and smart money signals by monitoring volume/OI ratio spikes, large block trades, unusual strike/expiry combinations, and net premium flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance-focused agents use this skill to answer ticker-specific or market-wide scan requests about unusual options activity, institutional flow, sentiment, net premium flow, and historical signal accuracy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may be overread as financial advice for trading decisions. <br>
Mitigation: Treat outputs as market-analysis assistance, verify against primary market data, and do not use the skill as the sole basis for financial decisions. <br>
Risk: Broad trigger terms may route ordinary options-flow discussions through this skill. <br>
Mitigation: Confirm that the user is asking for unusual options activity or options-flow analysis before applying the skill. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-unusual-activity) <br>
- [Publisher profile](https://clawhub.ai/user/clementgu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text summarizing unusual options activity and sentiment signals.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ticker symbols, scan filters, trade classifications, sentiment, net premium flow, smart money score, and historical accuracy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
