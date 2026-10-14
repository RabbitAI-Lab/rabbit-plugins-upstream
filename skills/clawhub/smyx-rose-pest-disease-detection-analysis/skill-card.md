## Description:

Analyzes rose images or videos for common pests and diseases, reporting severity and general care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and rose growers use this skill to assess photos or videos of leaves, shoots, and buds for possible pests or diseases, review severity, and get general care suggestions. They can also request account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rose images, videos, or URLs are sent to the publisher's cloud service.

Mitigation: Only submit media or URLs you are comfortable sharing with that service.

Risk: The skill silently creates or reuses a persistent local identity and stores tokens in the workspace data area.

Mitigation: Install only in a protected, non-shared directory and review local data access.

Risk: Cloud history queries access account-linked reports.

Mitigation: Review access to the associated account and use history queries only when appropriate.

Risk: Generic or pet-analysis code mismatches and an unsafe import path may not match the rose-diagnosis purpose.

Mitigation: Review before installing and ask the publisher to correct the import path and align the API references.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or be saved to a file.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
