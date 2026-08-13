## Description:

Analyzes child study-area images or video from a smart desk lamp or tabletop camera to estimate face orientation, gaze direction, fidgeting behavior, per-minute focus scores, distraction periods, and related focus reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and education-product developers can use this skill to analyze child study-area recordings, produce structured focus and distraction metrics, and retrieve historical focus reports. It is intended as a learning-behavior support tool and does not replace guardian or teacher judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send child study-area video, derived attention metrics, identity values, and report history to configured lifeemergence.com services.

Mitigation: Use only with guardian or institutional consent, avoid sensitive recordings, and review the remote service's account, token, retention, report-link, and deletion handling before deployment.

Risk: The skill silently manages cloud identities, accounts, tokens, and historical report access.

Mitigation: Confirm identity and token handling with the publisher, restrict deployment to approved environments, and review account/report access controls before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON structured analysis reports, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focus scores, distraction-event statistics, historical report tables, and remote report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
