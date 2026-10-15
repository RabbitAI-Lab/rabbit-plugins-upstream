## Description:

Creates keyword- or subject-focused highlights from videos and returns analysis results and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People organizing home videos, travel footage, or event recordings use this skill to find moments matching chosen subjects or keywords, request condensed highlights, and view current or past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal videos or video URLs may be sent to Life Emergence cloud services.

Mitigation: Obtain explicit approval before uploading media or sending video URLs; avoid sensitive footage unless cloud processing is acceptable.

Risk: History reports may be tied to an automatically created or reused account identity.

Mitigation: Confirm before querying report history, especially on shared machines, and review which account's reports may be exposed.

Risk: Service tokens are persisted in the workspace data directory.

Mitigation: Restrict workspace access and protect or remove stored tokens when the skill is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [Time-lapse analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Report links]

**Output Format:** [Text or JSON analysis results; Markdown table for history reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a file; generated highlights are accessed through service report links.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; artifact frontmatter lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
