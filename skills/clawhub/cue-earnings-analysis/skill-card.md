## Description:

Uses Cue to analyze listed companies’ latest disclosed financial results and produce a source-linked earnings commentary on performance drivers, profit quality, industry position, and financial risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors use this skill to understand a listed company’s disclosed financial results, track holdings, compare peers, and support an initial fundamental-screening step. It produces sourced analysis, not a substitute for independent investment judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Cue API key, which could be exposed through chat, shell history, or an overly permissive configuration file.

Mitigation: Have the user create and manage their own key; keep it out of chat and shell history, and restrict access to the configuration file.

Risk: The workflow relies on an external runner and requires network access; weakening agent protections increases exposure.

Mitigation: Review and pin the runner before use, allow only the required network connection, and keep the agent sandbox enabled.

Risk: Queries to Cue may consume account credits.

Mitigation: Tell the user that a query may incur credit usage and confirm the intended analysis before submitting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-earnings-analysis)
- [CNINFO disclosures](https://www.cninfo.com.cn)
- [SEC EDGAR company filings](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown earnings commentary with cited source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers disclosed financial results; analysis quality and timeliness depend on Cue and its external data sources.]

## Skill Version(s):

1.0.10

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
