## Description:

Analyzes pet grooming images or videos with server-side APIs to estimate coat matting, shed hair volume, grooming effectiveness, and hairball risk for pet-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care developers use this skill to submit grooming-area media or media URLs and receive structured coat-condition, shed-hair, grooming-effectiveness, and hairball-risk reports. It can also retrieve prior cloud reports associated with the internally resolved account identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or media URLs are sent to the provider's cloud service for analysis.

Mitigation: Use the skill only with media that may be shared with the provider, and avoid submitting sensitive or unnecessary background content.

Risk: The skill silently creates or reuses an account identity and stores authentication tokens in the workspace data directory.

Mitigation: Review the identity and token storage behavior before installation, and remove or isolate those features when a one-time analysis workflow is sufficient.

Risk: The history feature can retrieve prior cloud reports associated with the resolved identity.

Mitigation: Disable or restrict history retrieval unless users expect cloud report lookup for that identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [Grooming analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown report or JSON analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured analysis fields, care suggestions, report links, or Markdown tables for historical cloud reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
