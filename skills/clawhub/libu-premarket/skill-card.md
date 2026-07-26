## Description: <br>
礼部侍郎 is an A-share premarket planning skill that combines capital-flow signals, financial filters, and technical indicators to produce a premarket stock report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ygbeyond](https://clawhub.ai/user/ygbeyond) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill before the A-share market opens to gather global market context, prior-session sector signals, and filtered stock candidates for a premarket report. The output is for reference and does not constitute investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may import and execute code from a separate local tushare-finance skill path. <br>
Mitigation: Review the local tushare-finance skill before installation or run in an environment where only trusted local OpenClaw skills are present. <br>
Risk: The skill uses network market-data services and may produce stale, incomplete, or incorrect market context. <br>
Mitigation: Verify market data and generated stock candidates against trusted sources before acting on the report. <br>
Risk: The skill reads payment and market-data environment variables and writes cache, report, and payment-order files under ~/.openclaw. <br>
Mitigation: Run with least-privilege local access, provide only required environment variables, and review generated files before sharing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ygbeyond/skills/libu-premarket) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/ygbeyond) <br>
- [Tushare Pro](https://tushare.pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [JSON data file plus console text for Markdown-ready premarket reporting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes pre_market_data.json under the local OpenClaw workspace and uses local cache, market-data services, and ClawTip payment-order files when run.] <br>

## Skill Version(s): <br>
14.0.11 (source: server release metadata; artifact frontmatter and manifest report 14.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
