## Description: <br>
Stock Info Explorer uses Yahoo Finance via yfinance to fetch quotes and OHLCV data, summarize fundamentals, compute local technical indicators, and generate text reports, ASCII trends, and PNG charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kys42](https://clawhub.ai/user/kys42) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to request ticker-level market snapshots, fundamentals, historical trends, technical indicator summaries, and local chart files for financial research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested ticker symbols are sent to Yahoo Finance through yfinance. <br>
Mitigation: Use only ticker requests that are acceptable to disclose to Yahoo Finance and follow applicable data-provider terms. <br>
Risk: The local Python helper installs third-party Python packages and writes ticker-named chart images under /tmp. <br>
Mitigation: Run the helper in a managed environment and remove generated chart files when they are no longer needed. <br>
Risk: Market data quality can vary by ticker or market, including missing volume or incomplete history. <br>
Mitigation: Validate important outputs against authoritative financial data before using them for decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files] <br>
**Output Format:** [Terminal text tables, ASCII charts, and PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated chart images are saved under /tmp with ticker-based filenames, and report output may include CHART_PATH lines.] <br>

## Skill Version(s): <br>
1.2.10 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
