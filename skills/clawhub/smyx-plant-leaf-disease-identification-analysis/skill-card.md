## Description:

Identifies likely plant leaf diseases from leaf image or video inputs by analyzing lesion features and returning a structured report with confidence scores and general prevention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze plant leaf images, videos, local files, or URLs for likely disease type, confidence, and general prevention direction. It is suited for plant factories, greenhouses, home gardening, farm inspection, and horticultural maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs may be sent to lifeemergence.com services for analysis.

Mitigation: Use only non-sensitive plant media and confirm external cloud processing is acceptable before installation.

Risk: The skill may silently create or reuse a persistent identity and store local token data in the workspace.

Mitigation: Install only in workspaces where persistent account-linked identity behavior is acceptable, and clear local identity or token data when retiring the skill.

Risk: Historical report queries may access account-linked report history.

Mitigation: Limit use to accounts where report history access is expected and review retention and account behavior before deployment.

Risk: Disease identification results may be uncertain for unclear images, similar symptoms, or mixed infections.

Mitigation: Treat results as diagnostic support, use clear close-range images, and consult plant health experts for high-impact treatment decisions.

## Reference(s):

- [Plant Leaf Disease Identification API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease identification results, confidence scores, general prevention guidance, report links, or a Markdown table of historical reports.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
