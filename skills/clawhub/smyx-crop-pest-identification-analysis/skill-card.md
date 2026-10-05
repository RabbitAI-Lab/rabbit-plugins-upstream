## Description:

Analyzes crop images or videos through a remote service to identify common pests and return a structured report with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agronomists can submit crop photos or videos to identify common pests and review past reports. Results support field inspection, not pesticide-use recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently create or reuse an account identity and store tokens locally.

Mitigation: Review the identity behavior before installation and protect access to the workspace where credentials are stored.

Risk: Crop media and report-history queries are sent to configured cloud services without an explicit confirmation prompt.

Mitigation: Use only media and report history you are willing to share with the configured service; review cloud access before running the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [Crop pest identification API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pest types, estimated counts, confidence scores, a report link, or an optional saved result file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
