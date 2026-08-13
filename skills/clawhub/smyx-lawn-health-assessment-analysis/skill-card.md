## Description:

Assesses top-down lawn images or videos to estimate yellowing, weed coverage, bare soil, and an overall lawn health score for maintenance decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and facility managers use this skill to analyze lawn imagery from courtyards, golf courses, parks, sports fields, or similar green spaces and receive health metrics, maintenance guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lawn images or videos, report metadata, and account-like identifiers to LifeEmergence services.

Mitigation: Use it only with non-sensitive property imagery unless the publisher documents data retention, deletion, and authorization boundaries.

Risk: The skill creates or reuses an identity and stores reusable tokens locally in the workspace data directory.

Mitigation: Run it in a controlled workspace, restrict access to local data directories, and clear stored identity or token data between users or tenants.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and tables, with JSON detail mode and optional output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes image or video inputs and may return cloud-hosted report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
