## Description:

Create a shareable RooQuiz preview quiz - a right/wrong assessment where correct answers earn points and the taker gets a score - and get a link to open in the browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloevib](https://clawhub.ai/user/chloevib)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build a valid RooQuiz knowledge-quiz JSON payload, send it to RooQuiz's public preview endpoint, and return a temporary browser-openable preview link for review or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz text, answer keys, result copy, CTA URLs, and any lead-capture fields are sent to RooQuiz to create a temporary public preview link.

Mitigation: Use only content intended for RooQuiz preview creation, and avoid private, regulated, proprietary, or personal data unless that sharing is intended.

Risk: The preview link is temporary and public to anyone who has the link.

Mitigation: Treat preview URLs as shareable review links, avoid relying on them for persistence, and publish through RooQuiz only when the quiz should be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chloevib/skills/preview-quiz)
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms)
- [RooQuiz preview app](https://quizster.app)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON payloads, HTTP examples, shell command snippets, and a preview URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a temporary RooQuiz preview link that the source skill describes as short-lived, about one hour.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
