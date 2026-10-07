## Description:

Analyzes cat-tree videos supplied as local files or URLs to report activity by region, dwell times, transitions, and a 2D activity heatmap without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and pet-care teams use video of a cat tree to review cats' activity distribution, time spent at different levels, and movement between regions. They can also retrieve past analysis reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home footage, including submitted video URLs, is sent to an external cloud service.

Mitigation: Use only footage you are comfortable sharing; avoid sensitive home video and ask the publisher about retention and deletion before broad use.

Risk: The skill silently creates or reuses cloud identities and caches identity tokens in a local workspace database.

Mitigation: Run it in a separate workspace and ask the publisher to document authentication and token handling.

Risk: Network access is not tightly scoped to a single endpoint.

Mitigation: Review and restrict outbound access to approved service endpoints before deployment.

## Reference(s):

- [Activity heatmap API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured activity analysis or historical report list in text, Markdown, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include report links and be saved to a local file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
