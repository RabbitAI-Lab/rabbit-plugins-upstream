## Description: <br>
Analyzes A-share stocks with ChanLun technical-analysis methods, fetching K-line data, identifying structures such as fractals, strokes, central regions, and MACD divergence, then returning structured buy/sell signals and trading-reference guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hunkguo](https://clawhub.ai/user/hunkguo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to run ChanLun-based technical analysis on A-share stock codes, inspect current trend context, and draft trading-reference explanations. The output is reference material only and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate investment-related buy/sell suggestions from technical indicators. <br>
Mitigation: Treat all generated signals as reference material only, include the required investment-risk disclaimer, and verify decisions with independent analysis rather than relying on the skill as financial advice. <br>
Risk: The skill fetches public quote data over the network and caches market data in a temporary local folder. <br>
Mitigation: Install and run it only in environments where outbound market-data access and temporary local caching are acceptable, and verify dependencies before installation. <br>


## Reference(s): <br>
- [Chan Signal ClawHub page](https://clawhub.ai/hunkguo/skills/chan-signal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON analysis results plus Markdown-ready explanatory guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include stock code, period, latest price context, ChanLun structure counts, buy/sell signals, confidence scores, and a required investment-risk disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
