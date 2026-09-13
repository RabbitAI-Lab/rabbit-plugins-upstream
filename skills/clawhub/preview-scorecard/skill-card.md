## Description:

Create a shareable RooQuiz preview scorecard: a scored questionnaire where each option adds points toward a total that maps into result levels, then return a browser-openable preview link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloevib](https://clawhub.ai/user/chloevib)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to construct RooQuiz scorecard JSON, submit it to the RooQuiz preview service, and return a temporary preview link for self-assessments, habit checks, maturity checks, satisfaction surveys, or other scored questionnaires.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scorecard form content is sent to RooQuiz's preview service.

Mitigation: Do not include secrets, regulated data, proprietary questionnaires, or sensitive personal details unless that sharing is intended; use a self-hosted endpoint for stricter privacy requirements.

Risk: Preview links are temporary and expire after about one hour.

Mitigation: Use the preview link only for short-term review, or publish the form through RooQuiz if a persistent version is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chloevib/skills/preview-scorecard)
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz preview browser base](https://quizster.app)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a short-lived preview link; no account, login, API key, or credentials are required.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
