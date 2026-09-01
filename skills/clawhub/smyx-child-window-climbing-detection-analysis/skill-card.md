## Description:

Using fixed cameras in living rooms or child-activity areas aimed at windows or balconies, this skill analyzes video to detect child window or balcony climbing, leaning out, or gripping window-sill edges and returns warning-oriented results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, kindergartens, child activity centers, and smart-home or security integrators use this skill to analyze window or balcony camera footage for child fall-risk behaviors and produce structured alerts and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends child or home camera footage, or video URLs, to a cloud service for processing.

Mitigation: Use only with guardian consent and after verifying authorization, retention, access-control, deletion, and report-link expiry practices for the backend.

Risk: The skill silently manages account identity, tokens, and report history.

Mitigation: Review identity handling before deployment and avoid exposing continuous private feeds or sensitive URLs unless storage and access controls are verified.

Risk: Warning results may be incomplete, delayed, or incorrect and should not replace adult supervision.

Mitigation: Treat results as auxiliary alerts, maintain adult supervision, and review the skill before installing or deploying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text with warning details, structured analysis fields, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis output to a file when an output path is provided.]

## Skill Version(s):

1.0.10 (source: server release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
