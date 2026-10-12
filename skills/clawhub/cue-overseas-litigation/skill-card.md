## Description:

Helps research publicly available overseas litigation decisions and regulatory notices, summarizing case patterns and compliance implications for Chinese organizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and business teams use the skill to survey public cross-border cases and regulatory actions, compare outcomes, and identify potential implications for Chinese organizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a frequently updated external runner may execute unreviewed code.

Mitigation: Review the runner source before installation and pin a reviewed commit rather than pulling mutable code.

Risk: The API key is stored locally in plaintext and could be exposed.

Mitigation: Restrict file permissions, avoid shared machines and logged shells, and rotate the key if exposure is suspected.

Risk: Incomplete public-record coverage or inaccurate summaries could mislead legal decisions.

Mitigation: Check cited primary records and obtain qualified legal review before relying on the report.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue platform](https://cuecue.cn)
- [External Cue runner referenced by the skill](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Chinese-language Markdown report with case summaries and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local report copy and a link to the original report when available.]

## Skill Version(s):

1.2.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
