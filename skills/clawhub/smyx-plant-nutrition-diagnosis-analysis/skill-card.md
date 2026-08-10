## Description:

Diagnoses plant nutrient deficiency or excess from plant leaf images, videos, or URLs and returns structured findings with fertilization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, agronomists, and agent developers use this skill to analyze plant leaf media for nutrient deficiency or excess and receive structured diagnostic results, likely causes, fertilization suggestions, and report links. It can also retrieve prior cloud reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files or media URLs are sent to external cloud services for diagnosis.

Mitigation: Use only images, videos, or URLs that the user is permitted to upload to the configured service, and avoid sensitive or private plant-site imagery unless that cloud processing is acceptable.

Risk: The skill can create or reuse an account-linked identity and persist tokens locally.

Mitigation: Install only in workspaces where local credential persistence is acceptable, and review or clear stored identity material before sharing the workspace.

Risk: The skill can retrieve prior cloud report history for the resolved identity.

Mitigation: Confirm that report history access is intended for the current user or workspace before running report-list commands.

Risk: Plant nutrition diagnoses and fertilization recommendations may be incomplete or unsuitable for local growing conditions.

Mitigation: Treat results as advisory and combine them with soil testing, crop context, and local agricultural guidance before changing fertilization plans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrition-diagnosis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured text, with optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic findings, physiological cause analysis, fertilization suggestions, report lists, and report export links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
