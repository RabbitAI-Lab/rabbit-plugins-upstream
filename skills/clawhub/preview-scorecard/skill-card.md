## Description:

Create a shareable RooQuiz preview scorecard: a scored questionnaire where options add points toward a total that maps into result levels and returns a temporary browser link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft a scored self-assessment, readiness check, satisfaction survey, or similar questionnaire and generate a temporary RooQuiz preview link without credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questionnaire content is sent to the RooQuiz preview service and may be shared through a public temporary link.

Mitigation: Review content before creating previews and avoid private, regulated, or confidential data unless that use fits the user's data-handling requirements.

Risk: Preview links are short-lived and may stop working after expiration.

Mitigation: Treat generated links as temporary previews and recreate or publish through RooQuiz when a persistent form is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-scorecard)
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz preview link base](https://quizster.app)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and a browser-openable preview URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces temporary RooQuiz preview links that expire after about one hour.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
