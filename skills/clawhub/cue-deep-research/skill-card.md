## Description:

Conducts cross-validated research across public company, industry, market, regulatory, and legal information sources, and produces reports with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to research public companies, industries, competitors, and regulatory or market developments. It returns a structured Markdown report with cross-checked findings and links to cited sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes research as excluding personal data while also covering executive, litigation, penalty, and ownership records that may concern identifiable people.

Mitigation: Clarify the scope and lawful basis of person-related research, treat these records as personal information, and avoid sensitive queries or uploaded style documents.

Risk: The setup instructions download and run a Cue runner whose version is not pinned.

Mitigation: Review the runner source before execution and verify the version and changes being installed.

Risk: The skill requires a Cue API key and may send research prompts or reference documents to the service.

Mitigation: Configure the API key locally and do not submit confidential, sensitive, or otherwise restricted information.

## Reference(s):

- [Cue service](https://cuecue.cn/)
- [Cue API key registration](https://cuecue.cn/api-key?src=clawhub-deep-research)
- [Cue runner source (GitHub; referenced by the skill, not verified import provenance)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror (Gitee)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Structured Markdown research report with source links, saved as a local Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are intended to cite public sources; the skill also provides setup and usage guidance.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
