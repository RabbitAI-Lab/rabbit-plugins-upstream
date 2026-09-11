## Description:

Uses Cue to analyze the latest disclosed earnings reports for public companies, covering revenue and profit changes, business drivers, earnings quality, supply-chain leverage, financial risk signals, and cited source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and agents use this skill to request a sourced earnings commentary for A-share, Hong Kong, or U.S. public companies with already disclosed financial reports. The skill is intended for financial statement analysis and comparison, not unpublished forecasts, insider information, technical trading signals, or real-time market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow asks users to run unpinned code from an external Cue runner repository.

Mitigation: Review the runner before installation and use a pinned, verified commit rather than an unqualified branch checkout.

Risk: The Cue API key is stored locally in ~/.cue/config.json.

Mitigation: Restrict the config file to owner-only access and rotate the API key if the file may have been exposed.

Risk: Research queries and company-analysis inputs are sent to the Cue service.

Mitigation: Use the skill only with trusted Cue services and avoid confidential, non-public, or regulated research inputs.

Risk: The skill produces financial-analysis commentary that may be used in investment workflows.

Mitigation: Treat the output as sourced research support, verify source links and figures, and avoid relying on it as sole investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue API key portal](https://cuecue.cn/hub/api-key)
- [Cue sample earnings report](https://cuecue.cn/share/FKeQR7E8)
- [CNINFO](https://www.cninfo.com.cn)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with cited source links and inline shell commands for setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Cue template_id template_7qiAwz and can save reports as Markdown; optional conversion to DOCX or PDF is described by the skill.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
