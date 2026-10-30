## Description:

Generates condensed album highlights from long videos based on specified keywords or targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to find and summarize moments in long videos, such as home, travel, or event footage, and review the resulting analysis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option can still upload videos.

Mitigation: Wait for the export-only behavior to be fixed before relying on it; confirm the provider's retention policy and explicitly accept remote uploads before processing private footage.

Risk: Account registration and local token storage occur without clear user control.

Mitigation: Before use with private footage, explicitly accept account registration and local token storage.

Risk: Target-keyword customization needs repair.

Mitigation: Wait for target-keyword customization to be repaired before relying on customized extraction.

## Reference(s):

- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured analysis results and report links, with optional saved output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recognition results, suggestions, and links to reports.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
