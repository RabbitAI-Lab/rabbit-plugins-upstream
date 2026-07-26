## Description: <br>
Outer Ratio Monitor monitors selected A-share stocks by fetching public Tencent market data, calculating outer/inner volume ratios, and surfacing configured threshold changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoranyt](https://clawhub.ai/user/guoranyt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and market-monitoring users can run this skill to scan a configured A-share watchlist, review terminal output, and receive threshold-based alerts. Its outputs are technical market indicators and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global use; market data and example watchlists focus on China A-share securities. <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces financial-market signals that users could mistake for investment advice. <br>
Mitigation: Treat outputs as technical indicators only; review the skill's disclaimer and make independent investment decisions. <br>
Risk: The skill records stock watchlist snapshots and history locally under ~/.openclaw/memory/stocks. <br>
Mitigation: Review or delete local history files according to your privacy and retention needs before and after running the skill. <br>
Risk: Default watched stocks, thresholds, and alert behavior may not match a user's risk tolerance or market assumptions. <br>
Mitigation: Edit the watchlist, thresholds, and optional webhook settings before relying on alerts. <br>


## Reference(s): <br>
- [Outer Ratio Guide](references/outer_ratio_guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/guoranyt/skills/outer-ratio-monitor) <br>
- [Tencent Market Data Endpoint](https://qt.gtimg.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text, Markdown guidance, and configurable Python command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local stock watchlist history under ~/.openclaw/memory/stocks when run.] <br>

## Skill Version(s): <br>
2.4.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
