## Description:

Runs Cue's U.S. investment research workflow to produce source-linked draft research on U.S. equities, macro indicators, SEC filings, institutional holdings, COT positioning, fiscal liquidity, industry trends, and U.S. research funding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and investment research teams use this skill to run Cue workflows for U.S. equity and macro research, then review source-linked draft reports before acting on conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may clone or update an external Cue runner and execute it from the user's home directory.

Mitigation: Review the runner source and pin or control the installed runner version before use in restricted environments.

Risk: The workflow may read a local Cue API key, make network calls to Cue, and consume Cue credits after confirmation.

Mitigation: Confirm the intended Cue account, API key, and credit use before starting each deep research run.

Risk: The reports are based on public data and are not a substitute for due diligence, legal review, underwriting, or investment approval.

Mitigation: Keep source links intact and require qualified review before relying on the report for financial or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-us-research)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner on GitHub](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown research report with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue account/API key, live playbook lookup, credit confirmation, and public-source review.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
