## Description:

Create a shareable RooQuiz preview quiz - a right/wrong assessment where correct answers earn points and the taker gets a score - and get a link to open in the browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to create temporary scored quizzes, tests, trivia, or exams from structured JSON and return a browser-openable RooQuiz preview link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz content is sent to a third-party preview service when using the default cloud endpoint.

Mitigation: Use the skill for non-sensitive quizzes, and use documented self-hosted endpoint overrides for sensitive deployments.

Risk: Temporary preview links expire automatically and are not permanent published quizzes.

Mitigation: Recreate or publish the quiz through RooQuiz when a long-lived form is needed.

## Reference(s):

- [RooQuiz preview create endpoint](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz preview link base](https://quizster.app)
- [Preview Quiz on ClawHub](https://clawhub.ai/rooquiz/skills/preview-quiz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples, HTTP requests, shell commands, and a generated preview URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates short-lived preview links that expire after about one hour; supports endpoint overrides for self-hosted RooQuiz deployments.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
