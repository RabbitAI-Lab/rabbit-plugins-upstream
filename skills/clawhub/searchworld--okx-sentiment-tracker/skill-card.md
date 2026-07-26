## Description: <br>
Tracks crypto news, coin sentiment, social trend rankings, and macroeconomic calendar signals through read-only OKX CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to build crypto market briefings, coin-specific news searches, sentiment analyses, anomaly reports, and macroeconomic calendar summaries from OKX data. It is intended for read-only market intelligence, not trading, account management, or price/candle retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The OKX npm CLI install downloads a persistent helper binary and requires trust in the OKX package. <br>
Mitigation: Install only if the OKX CLI package is trusted, prefer the pinned 1.4.0 release, and review the package before use. <br>
Risk: The skill uses live OKX credentials configured in ~/.okx/config.toml. <br>
Mitigation: Use a dedicated OKX profile or read-only subaccount API credentials where possible, and review the local OKX configuration before running commands. <br>
Risk: Briefings may combine OKX results with web-search results when OKX coverage is sparse. <br>
Mitigation: Label OKX API results separately from web-search context so users can judge source reliability. <br>
Risk: Economic-calendar queries have a strict rate limit and counterintuitive time-window parameters that can produce noisy or misleading results if used incorrectly. <br>
Mitigation: Use both time bounds for future-event windows, avoid repeated calls, and verify timestamps before presenting calendar results. <br>


## Reference(s): <br>
- [Cross-Skill Workflows](references/workflows.md) <br>
- [OKX](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON-producing CLI calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only OKX news and sentiment workflows; sparse OKX coverage may be supplemented with clearly labeled web-search context.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
