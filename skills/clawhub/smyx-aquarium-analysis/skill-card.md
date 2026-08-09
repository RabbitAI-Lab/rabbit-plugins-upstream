## Description:

When a user provides a video URL or file of aquatic pets such as goldfish, koi, betta, shrimp, crab, or related species, this skill calls a server-side API to analyze visible health indicators and produce an aquatic pet health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium caretakers use this skill to submit local media files or media URLs for fish and aquatic pet health analysis, including scale, fin, body color, activity, and disease-warning signals. The skill can also return cloud-stored historical report listings associated with the current internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads aquarium media or media URLs to lifeemergence.com services for analysis.

Mitigation: Use only with media the user is comfortable sending to the external service, and require clear consent before broad deployment.

Risk: The skill silently creates or reuses backend identities and stores account tokens in a local workspace database.

Mitigation: Administrators should scope permissions, document identity and token storage behavior, and provide a deletion process for local identity and token state.

Risk: The skill can query cloud report history associated with the current internal identity.

Mitigation: Limit report-history access to appropriate users and review the history command path before enabling the skill in shared environments.

Risk: The security verdict is suspicious because the advertised analysis is combined with identity, token, and cloud-history behavior users may not expect.

Mitigation: Review the ClawHub security summary and guidance before installation, and approve the skill only after consent, permissions, and deletion controls are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON health analysis report, with optional local output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API-backed analysis; documented media inputs include mp4, avi, and mov files up to 10 MB or public media URLs.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
