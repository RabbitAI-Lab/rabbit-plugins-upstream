## Description: <br>
Create a shareable RooQuiz preview quiz that scores right/wrong answers and returns a browser-openable temporary preview link without requiring an account, login, or API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rooquiz](https://clawhub.ai/user/rooquiz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to draft graded quizzes, submit them to RooQuiz's preview service, and receive a temporary browser link for review or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quiz text and answers are sent to RooQuiz's preview service to generate a temporary public-token link. <br>
Mitigation: Avoid putting private, regulated, or sensitive content into previews unless external hosting is acceptable. <br>
Risk: Preview links are temporary and may be shared with anyone who has the token, unless a secret is configured. <br>
Mitigation: Use the optional secret for restricted previews and recreate the quiz in RooQuiz when a permanent form is needed. <br>
Risk: Malformed quiz JSON can fail server validation and prevent preview creation. <br>
Mitigation: Follow the documented quiz schema, use valid identifiers for question and option codes, and correct any HTTP 400 validation errors before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-quiz) <br>
- [RooQuiz preview API endpoint](https://preview.rooquiz.com/api/preview-forms) <br>
- [RooQuiz preview link base](https://quizster.app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown with JSON, HTTP, and shell command snippets plus a preview link.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates short-lived RooQuiz preview links; user-provided quiz content is sent to RooQuiz's preview service.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
