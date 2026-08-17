## Description:

Analyzes fixed-camera child behavior videos to identify repetitive stereotyped behaviors such as spinning, hand flapping, and body rocking, then produces structured behavior statistics and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External therapists, caregivers, and rehabilitation teams use this skill to analyze uploaded or URL-based child behavior videos, generate structured event statistics, and retrieve prior cloud reports for longitudinal review. The output is descriptive support for professional review, not diagnosis or treatment prescription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-behavior videos or video URLs may be sent to lifeemergence.com services.

Mitigation: Use only where guardian consent, backend trust, retention rules, and approved upload paths are clear; prefer privacy-preserving skeleton or contour modes when available.

Risk: Cloud history and report retrieval may expose sensitive prior reports.

Mitigation: Confirm per-user workspace isolation, report access controls, and appropriate authorization before using history-list or report-export features.

Risk: Identity and session data may be persisted locally for reuse.

Mitigation: Review local storage and token handling before deployment, and clear or segregate workspace data on shared systems.

Risk: Behavior statistics may be mistaken for clinical diagnosis or intervention advice.

Mitigation: Treat outputs as descriptive observations for qualified professional review, and do not use them as a substitute for clinical assessment or therapy planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown and JSON-like structured reports with behavior events, summary metrics, trends, intervention hints, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report-list results and exported report-image links; output detail can be basic, standard, or json.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
