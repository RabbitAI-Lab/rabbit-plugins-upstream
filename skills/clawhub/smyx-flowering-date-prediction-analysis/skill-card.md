## Description:

AI-powered flowering-date prediction for ornamental and cut-flower plants, using flower-bud images and optional accumulated temperature and light data to estimate full bloom within 3–7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse growers, cut-flower producers, botanical gardens, and flower-tourism operators can use this skill to estimate flowering dates from bud images or video, optionally combined with temperature and light accumulation data, and plan pollination, harvesting, or visitor schedules. Predictions are for planning reference and should be checked against field observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill can register accounts silently and retain credentials.

Mitigation: Defer installation until account registration is clearly disclosed; protect credentials and restrict them to trusted destinations.

Risk: The security review reports that media may be uploaded even when `--export-env-only` is specified.

Mitigation: Do not provide sensitive imagery, and verify that this option prevents analysis before relying on it.

Risk: The security review says service charges, data retention, and account deletion options need confirmation.

Mitigation: Confirm charges, retention practices, and account deletion options before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON or Markdown analysis report with flowering-date estimates, bud-stage findings, confidence information, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts image or video inputs; predictions are estimates for planning and the skill documentation notes an approximate ±1–2 day error.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
