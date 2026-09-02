## Description:

Using fixed cameras in malls, exhibition halls, scenic areas and other public places, the skill analyzes anonymous group facial-expression signals, summarizes emotion distribution, and computes a group emotion index for operational insight and safety awareness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Facility operators, security teams, and analytics developers use this skill to process public-place camera video or image inputs and produce anonymous, aggregate emotion metrics, regional breakdowns, operational suggestions, safety guidance, and historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-camera emotion analysis may be unlawful or inappropriate without notice, consent handling, and a valid operating basis.

Mitigation: Use only in approved locations with visible notice, documented governance, and human review of any operational or safety response.

Risk: Media files or URLs are sent to a configured remote service for analysis.

Mitigation: Confirm the remote service, retention policy, access controls, and data-transfer approvals before deployment.

Risk: The skill silently creates or reuses identity data and stores tokens in a sensitive workflow.

Mitigation: Remove or formally govern silent account creation, local persistence, and token storage before using it in anonymous-only deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and JSON-formatted text with analysis results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aggregate emotion distributions, group emotion index, regional breakdowns, alert levels, heatmap/report URLs, or historical report tables.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
