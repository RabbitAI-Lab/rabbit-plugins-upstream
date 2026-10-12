## Description:

Analyzes published earnings reports for listed companies, covering financial performance, business drivers, cash-flow quality, and potential financial risks in a sourced commentary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and analysts use this skill to review publicly disclosed earnings for listed companies and compare financial health using source-linked reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external research runner may change after installation.

Mitigation: Review and pin the runner before executing it with a reusable or paid API key.

Risk: A locally stored plaintext API key could be exposed to other users or processes.

Mitigation: Use restrictive file permissions or an environment variable for the key.

Risk: Company queries are sent to Cue's external service, and report quality depends on its data sources.

Mitigation: Share only queries appropriate for an external service and check cited filings before relying on conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue research runner referenced by the skill (not verified release provenance)](https://github.com/sensedeal/cue-skills)
- [Cue platform](https://cuecue.cn/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown earnings commentary with source links and a link to the original Cue report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers published financial statements; may be saved locally as a Markdown report.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
