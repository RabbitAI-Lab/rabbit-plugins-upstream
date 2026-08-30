## Description:

Analyzes fixed-angle indoor plant images or video to detect leaf aging signals and predict leaf fall risk windows over the next 3-7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze continuous indoor plant media for leaf color, gloss, and petiole-angle changes, then receive structured leaf aging reports, fall-risk windows, and care guidance. The skill also supports cloud history lookups for prior leaf aging and fall prediction reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs may be sent to the Life Emergence backend for analysis.

Mitigation: Use media approved for upload and confirm the service's retention, access, and account controls before deployment.

Risk: The skill can create or reuse a local/cloud identity and store service tokens in the workspace data directory.

Mitigation: Run it in an isolated workspace, review token storage practices, and clear local data when reports or credentials should not persist.

Risk: Default configuration includes development HTTP endpoints that may be unsuitable for production use.

Mitigation: Review and replace endpoint configuration with approved production services before commercial operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [Leaf Aging Fall Prediction API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Usage Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text with optional shell commands and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured analysis content, fall-risk timing, at-risk leaf identifiers, care suggestions, and historical report tables when requested.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
