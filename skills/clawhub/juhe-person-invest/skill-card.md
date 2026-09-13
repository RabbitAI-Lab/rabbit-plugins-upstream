## Description:

Queries Juhe's person investment and appointment API for a person's external investments, corporate roles, shareholding relationships, subscribed capital, and business status using a name, national ID number, and optional mobile number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform authorized due-diligence lookups for a natural person's company investments, legal-representative roles, executive roles, and shareholder relationships through Juhe's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes national ID, mobile, and corporate-affiliation data, and the security summary notes that raw identifiers may be exposed in logs or transcripts.

Mitigation: Use the skill only when authorized to process the subject's data, avoid shared transcripts and logs, and keep displayed identifiers masked.

Risk: Queries send a person's name, national ID number, and optional mobile number to juhe.cn.

Mitigation: Confirm user consent and data-transfer authorization before querying, and do not use command-line API keys or identifiers in shared environments.

Risk: The security verdict is suspicious because privacy guardrails are limited for real-person lookup workflows.

Mitigation: Review the workflow before installation and fix or disable the default raw JSON output before use with real people.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-person-invest)
- [Juhe person investment API documentation](https://www.juhe.cn/docs/api/id/320)
- [Juhe data platform](https://www.juhe.cn)
- [Juhe person investment API endpoint](https://apis.juhe.cn/personinvest/query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown-oriented guidance with shell command examples and formatted text or JSON lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JUHE_PERSON_INVEST_KEY; sends the subject's name, national ID number, and optional mobile number to juhe.cn.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
