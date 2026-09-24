## Description:

Analyzes transparent-pot or smart-seedling-box root images and videos to report root color, root hair density, branching, rot signs, a 0-100 health score, vitality grade, care guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze clear images, videos, or URLs of visible plant roots in transparent pots, smart seedling boxes, plant factories, and hydroponic systems. It helps identify visual root-health issues early and returns care-oriented guidance without specific drug-use advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and history queries are sent to the Life Emergence cloud service.

Mitigation: Use the skill only with imagery and URLs suitable for that cloud service, and avoid sensitive visual content unless data handling has been reviewed.

Risk: The scanner reports that the skill can silently create or reuse a local service identity and store account tokens in workspace data.

Mitigation: Review local workspace data and account behavior before installation, especially in shared workspaces.

Risk: Historical report queries can fetch account-linked prior analysis records.

Mitigation: Confirm that account association and report visibility are appropriate before using history-list features.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-style analysis, history-report tables, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a requested file path; history queries return account-linked cloud report records.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
