## Description:

Supports uploading local MP4 videos or network video URLs to call a server-side API for facial diagnosis and return structured TCM facial diagnosis results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit facial videos or video URLs for server-side TCM-style facial analysis, then receive structured results, health warnings, suggestions, and report links. It can also retrieve cloud-hosted historical facial analysis reports associated with the managed user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial videos or video URLs are sent to lifeemergence.com services for analysis.

Mitigation: Process only videos that the user has the right and consent to submit, and confirm that the remote service's data handling is acceptable for the intended use.

Risk: The skill can create or reuse a managed identity and store service tokens locally.

Mitigation: Review local workspace data, including managed identity and token storage, before uninstalling the skill, sharing the workspace, or moving it to another environment.

Risk: Cloud history retrieval can expose prior health-style reports associated with the managed identity.

Mitigation: Run history queries only in trusted workspaces and verify that the active identity is the expected one before retrieving report lists.

Risk: TCM facial diagnosis output may be incorrect or incomplete and is not a professional medical diagnosis.

Mitigation: Treat results as informational health references and route medical decisions to qualified professionals.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON analysis report with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report content to a user-specified output file.]

## Skill Version(s):

1.0.6 (source: frontmatter); release 999.999.999 (source: ClawHub metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
