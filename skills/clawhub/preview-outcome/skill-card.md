## Description:

Create a shareable RooQuiz preview personality or outcome test whose options vote for result types, then return a short-lived browser link without requiring an account, login, or API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to create temporary RooQuiz personality or archetype quiz previews, validate the required outcome-quiz JSON shape, and return a browser-openable preview link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz titles, questions, answers, and result text are sent to RooQuiz's public preview service and exposed through a shareable temporary link.

Mitigation: Do not include private, confidential, regulated, or sensitive information in preview quiz content.

Risk: The skill creates temporary previews rather than permanently published forms.

Mitigation: Recreate or publish the quiz through the appropriate RooQuiz workflow when a durable form is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-outcome)
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz preview link base](https://quizster.app)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples, HTTP request examples, shell commands, and a preview URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces short-lived RooQuiz preview links and does not require credentials.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
