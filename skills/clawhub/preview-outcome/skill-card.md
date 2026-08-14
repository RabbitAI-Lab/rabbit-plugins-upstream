## Description:

Creates temporary shareable RooQuiz personality or outcome-test previews where answer options vote for result types and the most-voted type is shown to the quiz taker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rooquiz](https://clawhub.ai/user/rooquiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to build RooQuiz outcome-test JSON, submit it to the RooQuiz preview service, and return a short-lived browser preview link. It is intended for trying and sharing personality, type, or archetype quizzes that do not have right or wrong answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz titles, questions, answers, and result text are sent to RooQuiz's preview service.

Mitigation: Avoid private or sensitive content in preview quizzes unless sharing that content with the preview service is acceptable.

Risk: Preview links are temporary and can be opened by anyone who has the token while the preview is live.

Mitigation: Use the optional secret when a preview should be harder to access before it expires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-outcome)
- [RooQuiz preview service](https://preview.rooquiz.com)
- [RooQuiz preview viewer](https://quizster.app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell command snippets, and a preview URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces temporary preview links that expire after about one hour; optional secret values can make links harder to access before expiry.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
