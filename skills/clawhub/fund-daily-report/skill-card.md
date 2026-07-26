## Description: <br>
Generates daily fund performance reports with NAV changes, market commentary, portfolio updates, and market flow rankings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors, analysts, and operations teams use this skill to generate daily Chinese fund market reports covering NAV leaders, ETF attention, industry fund flows, and high-attention stocks after market close. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The script contains an embedded JQData username and password and can silently use that account as a fallback data source. <br>
Mitigation: Remove and rotate the embedded credential before installation; require authenticated data providers to be configured through secrets or environment variables. <br>
Risk: Live market data calls can fail or be blocked by network controls, which may leave report sections incomplete. <br>
Mitigation: Run after market close with validated network access or proxy configuration, and review missing sections before relying on the report. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/fund-daily-report) <br>
- [README.md](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text report with tabular sections and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Depends on live AKShare, Eastmoney, and optional JQData availability; report sections may be incomplete when data providers or network access fail.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
