## Description:

Create a shareable RooQuiz preview personality or outcome test where answer options vote for result types, then return a browser-openable preview link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloevib](https://clawhub.ai/user/chloevib)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help people draft, validate, and submit temporary RooQuiz personality or archetype quizzes. It is intended for users who want a quick preview link without an account, login, API key, or permanent publication step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quiz content, images, and CTA URLs are sent to RooQuiz/Quizster to create the preview link.

Mitigation: Avoid including secrets or sensitive personal data in preview quiz text, images, or CTA URLs.

Risk: The preview defaults to Chinese if the language field is omitted.

Mitigation: Set the intended language explicitly, such as en_US for English.

Risk: Preview links are short-lived and are not permanent published quizzes.

Mitigation: Tell users that the preview expires after about one hour and must be published in RooQuiz to keep it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chloevib/skills/preview-outcome)
- [RooQuiz Preview API](https://preview.rooquiz.com/api/preview-forms)
- [Quizster Preview Link Base](https://quizster.app)

## Skill Output:

**Output Type(s):** [guidance, json, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a temporary RooQuiz preview link after submitting quiz JSON to the preview service.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
