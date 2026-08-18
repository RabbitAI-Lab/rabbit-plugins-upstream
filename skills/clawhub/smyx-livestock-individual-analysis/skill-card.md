## Description:

Identifies individual pigs, cattle, and sheep from face or body-pattern media and returns a stable individual ID, confidence, matched feature areas, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External farm operators and developers use this skill to send livestock images, short videos, or media URLs to a cloud analysis service for individual identification, tracking records, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud processing of livestock images, videos, and report history may expose operational farm media or records outside the local workspace.

Mitigation: Use the skill only when cloud processing is acceptable for the media and report history involved; avoid submitting unrelated sensitive content.

Risk: The skill silently creates or reuses an identity and stores auth tokens locally under the workspace data directory.

Mitigation: Review local data and token handling before deployment, restrict workspace access, and rotate or clear stored credentials when identities should no longer be reused.

Risk: Individual identification results are confidence-based and may not be sufficient for formal production, health, or breeding records without review.

Mitigation: Treat results as identity-association support and confirm important records against farm systems and human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured analysis report with individual ID, confidence, matched feature areas, report links, optional JSON detail, and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also return historical report listings as a Markdown table from the cloud report API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
