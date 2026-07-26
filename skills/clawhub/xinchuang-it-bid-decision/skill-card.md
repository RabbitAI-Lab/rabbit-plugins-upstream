## Description: <br>
Assists agents with evaluating Xinchuang and IT informationization bids by querying procurement history, competitor signals, pricing benchmarks, and producing decision reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams, proposal teams, and agents use this skill to decide whether to pursue IT, system integration, cloud, cybersecurity, data center, smart city, and Xinchuang procurement opportunities. It analyzes buyer history, incumbent suppliers, likely competitors, comparable pricing, qualification risks, and produces a traceable bid-decision report. <br>

### Deployment Geography for Use: <br>
Global; intended for Chinese IT procurement and Xinchuang bid data. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-register an account when no API key is configured, using a stable hashed MAC-derived device identifier for trial-usage deduplication. <br>
Mitigation: Prefer supplying ZLBX_API_KEY through a trusted secret mechanism; allow auto-registration only after explicit user consent and disclose the collected device attributes before registration. <br>
Risk: API keys may be stored locally and used for quota-consuming bid-data queries. <br>
Mitigation: Keep local credential files private, never paste API keys into conversation, and tell users the expected query-credit cost before running a full report. <br>
Risk: Generated reports and source links may contain signed access parameters or commercially sensitive project and company context. <br>
Mitigation: Review Markdown and HTML reports before sharing, treat report links containing signed parameters as sensitive, and remove or restrict links when distribution is not intended. <br>
Risk: Bid recommendations may be incomplete or misleading if public procurement data is missing, stale, or interpreted too strongly. <br>
Mitigation: Keep conclusions tied to cited data, mark data gaps and confidence levels, use cautious wording for real organizations, and treat reports as reference material rather than business, legal, or procurement advice. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/xinchuang-it-bid-decision) <br>
- [Workflow Guide](references/workflow.md) <br>
- [API Quick Reference](references/api-quick.md) <br>
- [Report Template](references/report-template.md) <br>
- [Auto-Registration Flow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, HTML, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown decision report with optional self-contained HTML report file and concise operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; full analysis usually consumes 12-25 query credits, while quick analysis uses about 5-8.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
