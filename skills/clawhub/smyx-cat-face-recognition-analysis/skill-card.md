## Description:

Identifies specific cats by comparing cat face images or videos against a preregistered database and can retrieve prior recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify individual cats from submitted images, videos, or URLs, especially in multi-cat households with a preregistered cat database. It also supports retrieving cloud-stored cat recognition report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local cat media or submitted URLs are sent to a remote service for analysis.

Mitigation: Use only media that the user is comfortable sending to the remote service, and avoid private surveillance footage unless consent, retention, and endpoint configuration are clarified.

Risk: Report history is queried from the cloud and associated with a local workspace identity.

Mitigation: Review account identity behavior before use, isolate workspaces for sensitive use cases, and avoid exposing report links or identity values in user-facing output.

Risk: The security evidence marks the release as suspicious because identity and token handling may be unexpected.

Mitigation: Review before installing, confirm token storage and endpoint configuration with the publisher, and remove shared local credentials after testing when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-cat-face-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Cat face recognition API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured recognition results, historical report lists, and report export links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
