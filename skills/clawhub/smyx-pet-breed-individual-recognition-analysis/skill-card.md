## Description:

Identifies cat and dog breeds in images or videos and helps distinguish individual pets in multi-pet households.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers can identify cats and dogs, distinguish individuals in multi-pet households, and retrieve previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and videos may be uploaded to Life Emergence services for analysis; the export-env-only option does not guarantee that media will not be uploaded.

Mitigation: Do not submit private household footage until the provider's retention policy has been verified, and do not rely on export-env-only to prevent uploads.

Risk: Shared accounts may expose other users' reports, and account setup may retain local credentials.

Mitigation: Avoid shared workspaces until sender isolation is fixed; use protected credential storage and HTTPS-only credential destinations.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured pet identification results and report links; report lists can be presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected pet counts, breed and individual identification, confidence values, and report links. Results are for pet interest and are not a substitute for professional breed verification.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
