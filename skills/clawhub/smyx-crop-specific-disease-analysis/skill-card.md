## Description:

Expands the disease identification library to cover economic-crop-specific diseases (corn northern/southern leaf blight, potato late blight, peanut leaf spot, tomato viral disease, etc.) for precise leaf-disease recognition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, agronomy users, and agents use this skill to analyze economic-crop leaf images or videos for crop-specific disease identification and to retrieve prior disease-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, or media URLs are sent to a remote LifeEmergence service for analysis.

Mitigation: Use the skill only with crop media that is acceptable to transmit to that service, and avoid including unrelated sensitive content in submitted media.

Risk: The skill can silently create or reuse account identity and persist returned tokens in workspace data.

Mitigation: Run it in a workspace with controlled access, and remove the workspace data database and any smyx API key file when uninstalling or rotating identity.

Risk: Historical report lookup depends on cloud-stored analysis history for the current identity.

Mitigation: Install it only where generated report history is acceptable to store and retrieve, and avoid sharing one workspace identity across unrelated users.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Crop disease API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown text with structured JSON analysis content, report links, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can submit local crop media or media URLs, poll for cloud analysis results, and return historical report lists.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
