## Description:

Analyzes fish-feeding videos to report feeding activity, remaining feed, and possible appetite decline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and developers use feeding videos or URLs to assess fish-feeding activity, review appetite alerts, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish-feeding videos or supplied URLs are processed by the Life Emergence cloud service.

Mitigation: Obtain informed consent before sharing media; confirm the service's retention and data-use terms.

Risk: The skill creates and reuses an account-linked identity and cached tokens for report history.

Mitigation: Review token storage, account access, and history-query controls before deployment.

## Reference(s):

- [Fish-feeding analysis API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [JSON or Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Feeding activity score, appetite alerts, and historical report listings when requested.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled skill frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
