## Description:

Analyzes full-body pet images or videos through server-side APIs to estimate breed or body type and fur density, then returns a non-medical drying temperature and duration curve for pet drying devices or grooming workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pet-care operators use this skill to submit pet images, videos, or URLs for breed/body-type and fur-density analysis, receive drying temperature and time recommendations, and query prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos may be uploaded to a configured cloud service for analysis.

Mitigation: Disclose cloud processing before use and require user confirmation before uploading media or analyzing remote URLs.

Risk: The skill can automatically create or reuse cloud-linked identity state and transmit tokens with limited user control.

Mitigation: Use fixed reviewed API endpoints, isolate runtime credentials, and apply a token storage, rotation, or deletion policy before production use.

Risk: History queries can retrieve cloud-stored reports linked to the current internal identity.

Mitigation: Require explicit confirmation before history queries and avoid using shared identities for sensitive or multi-user environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with JSON-style structured analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a cloud report export URL and can save output to a file when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
