## Description:

Analyzes fry tank images or videos with a known-size reference object to estimate body length and growth rate, produce growth reports, and flag growth or measurement concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculturists, ornamental fish breeders, and developers can use the skill to estimate fry length from images or video, track growth over time, and review structured reports or historical records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and credential handling, including credential-bearing requests to arbitrary URLs.

Mitigation: Before use, verify why account registration and credential storage are needed, and identify every destination that may receive credentials or video.

Risk: The security review reports behavior that does not match the advertised fry-growth purpose, and the scan is partial.

Mitigation: Review the skill before installation; prefer export-only mode if it meets the need, and verify whether it avoids analysis.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis reports in JSON and historical-record tables in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include measurements, growth statistics, trend information, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
