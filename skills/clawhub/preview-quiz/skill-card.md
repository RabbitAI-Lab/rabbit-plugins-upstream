## Description:

Create a shareable RooQuiz preview quiz with correct answers, scored results, and a browser-openable preview link without requiring an account, login, API key, or credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and content creators use this skill to draft a right/wrong assessment, create a temporary RooQuiz preview, and return a link that can be opened in a browser for review or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz titles, questions, answers, descriptions, and result text are sent to RooQuiz-hosted infrastructure to create the preview.

Mitigation: Do not include secrets, regulated personal data, proprietary exam content, or internal documents unless approved for upload to that service.

Risk: The skill returns a temporary browser preview link for user review or sharing.

Mitigation: Treat preview links as temporary review artifacts and use the optional secret when the quiz content should not be accessible with only the token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-quiz)
- [RooQuiz publisher profile](https://clawhub.ai/user/rooquiz)
- [RooQuiz preview API](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz browser preview base](https://quizster.app)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON examples, optional shell commands, and a preview link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a short-lived preview link; users may set a secret for preview access.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
