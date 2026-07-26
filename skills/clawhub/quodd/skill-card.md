## Description: <br>
Fetch real-time stock quotes via Quodd API, including current prices, daily high/low, and after-hours data for US equities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khaney64](https://clawhub.ai/user/khaney64) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve real-time US equity quote data from Quodd when a user asks for stock prices, market data, ticker quotes, or after-hours quote information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Quodd account credentials and caches a short-lived token locally. <br>
Mitigation: Install only if this credential use is acceptable; on shared machines, clear ~/.openclaw/credentials/quodd-token.json after use or ensure the file is readable only by the current user. <br>
Risk: Quote retrieval depends on Quodd API access, account permissions, network availability, and token freshness. <br>
Mitigation: Confirm Quodd credentials and permissions before use, and use --no-cache after credential changes or token-related authentication errors. <br>


## Reference(s): <br>
- [Quodd Stock and ETF Data](https://www.quodd.com/stock-and-etf-data) <br>
- [ClawHub Quodd Skill Page](https://clawhub.ai/khaney64/skills/quodd) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [Text table by default, or JSON when requested with --format json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and QUODD_USERNAME/QUODD_PASSWORD environment variables; accepts one or more ticker symbols and an optional --no-cache token refresh flag.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
