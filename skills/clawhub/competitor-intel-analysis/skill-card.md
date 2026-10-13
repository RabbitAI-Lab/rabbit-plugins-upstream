## Description:

Analyzes bidding competitors using procurement records to produce company intelligence reports and side-by-side comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams and procurement analysts assess a company's bidding history, customers, competitors, and public risk signals, or compare two companies before competing for business.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shareable reports include links that may open platform pages without a login.

Mitigation: Review report links and share generated HTML only with the intended audience.

Risk: Reports and API credentials are saved locally.

Mitigation: Prefer a preconfigured API key, review ~/.zlbx/config.json after use, and protect locally saved reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis)
- [Analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [API quick reference](artifact/references/api-quick.md)
- [Account setup and consent](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML]

**Output Format:** [Conversational Markdown and a locally saved HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company report or two-company comparison; optional concise weekly updates.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
