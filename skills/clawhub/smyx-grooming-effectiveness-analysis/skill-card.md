## Description:

Analyzes pet-grooming images, videos, or URLs through server-side APIs to estimate coat matting, shed-hair volume, grooming effectiveness, and hairball risk for pet-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care product teams use this skill to analyze grooming media, receive structured grooming-effectiveness and hairball-risk reports, and query prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or provided URLs are processed by the provider's cloud service.

Mitigation: Use only media appropriate for third-party cloud processing and review data-sharing expectations before deployment.

Risk: The skill silently creates or reuses a backend identity and may read a workspace identity file when present.

Mitigation: Review the identity behavior with users or operators before installation and avoid placing unintended identity values in the workspace data file.

Risk: Backend tokens may be stored in a local SQLite database for report history and API reuse.

Mitigation: Protect the workspace data directory, limit access to token-bearing files, and clear stored credentials when decommissioning the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Grooming Analysis API Document](references/api_doc.md)
- [SMYX Analysis API Document](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a user-specified file; history listings are returned from the provider cloud API.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
