## Description:

Customizes virtual safety zones for home monitoring videos, identifies infants crossing boundaries or approaching dangerous areas such as bedsides and windowsills, and returns alerts and structured analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and developers use this skill to analyze home monitoring video files or video URLs for virtual fence crossing alerts and to retrieve cloud-hosted historical alert reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home monitoring media and supplied video URLs are processed by LifeEmergence cloud endpoints.

Mitigation: Use only inputs approved for cloud processing and avoid sensitive footage unless external analysis is permitted.

Risk: The skill may create or reuse a persistent account identity and stored tokens in the workspace data directory.

Mitigation: Review workspace data storage and token handling before deployment, and restrict access to account-linked report history.

Risk: Virtual fence alerts are auxiliary safety signals and should not replace direct supervision or physical safeguards.

Mitigation: Keep human monitoring and physical safety measures in place when using the skill for infant safety scenarios.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Virtual fence analysis API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with JSON structured analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts mp4, avi, and mov video inputs up to 10 MB; can query cloud-hosted report history.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
