## Description:

Identifies individual pigs, cattle, and sheep from images or videos and returns identity matches and confidence information for livestock tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and developers use this skill to associate livestock images or videos with individual animal IDs, review confidence information, and retrieve past identification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock images, videos, and identity-linked report requests are sent to remote services.

Mitigation: Use only with approved media and accounts; confirm the service's access and retention practices before uploading.

Risk: Identity input and broad history-report triggers may expose reports beyond the intended request.

Mitigation: Restrict who can request report history, verify the selected identity and scope, and avoid broad report-list queries when unnecessary.

Risk: Local account records and cached tokens may be accessible to other users of the device.

Mitigation: Limit access to local account data and prefer a release that does not store tokens in plaintext.

## Reference(s):

- [Livestock identification API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis results; Markdown tables with links for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include matched animal IDs, confidence information, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
