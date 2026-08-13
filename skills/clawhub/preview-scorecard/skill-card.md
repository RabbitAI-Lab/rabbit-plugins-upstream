## Description:

Create temporary RooQuiz preview links for scored questionnaires where answer choices contribute points to a total score and result level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content authors use this skill to construct RooQuiz scored questionnaire JSON, submit it to a public preview endpoint, and return a short-lived browser link for review or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questionnaire content is sent to the configured RooQuiz preview service and may be viewable by anyone with the generated link if no secret is set.

Mitigation: Do not include private or sensitive personal data in preview forms, and set a secret when sharing should be limited.

Risk: Preview links are temporary and expire after about one hour.

Mitigation: Use previews for review and testing only; recreate the form in RooQuiz when a persistent version is needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rooquiz/skills/preview-scorecard)
- [RooQuiz Preview API](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz Preview Viewer](https://quizster.app)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces short-lived preview links and optional secret-protected links.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
