## Description:

Analyzes crop-leaf images and videos for crop-specific diseases and returns identification results and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisers use this skill to screen images or videos of corn, potato, peanut, and tomato leaves for crop-specific diseases and view analysis reports. Results are for preliminary identification, not a definitive diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied crop media is uploaded to lifeemergence.com for analysis.

Mitigation: Submit only non-sensitive crop images or videos and review the service's data-handling terms before use.

Risk: The skill silently creates or reuses a local identity and stores service tokens in a workspace SQLite database.

Mitigation: Avoid installation in workspaces where persisted identity or tokens are inappropriate; protect and remove local state according to your retention policy.

Risk: Historical report requests query cloud-held records, and visual disease identification may be uncertain.

Mitigation: Review report access and confirm consequential diagnoses with field observations or an agronomy expert.

## Reference(s):

- [Crop-specific disease analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured disease analysis or Markdown report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease type, confidence, symptoms, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.13 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
