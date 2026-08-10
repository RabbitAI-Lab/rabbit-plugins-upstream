## Description: <br>
Creates a shareable RooQuiz preview scorecard for scored questionnaires and returns a browser-openable temporary preview link without requiring an account, login, or API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rooquiz](https://clawhub.ai/user/rooquiz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and agents use this skill to turn a drafted self-assessment, maturity check, satisfaction survey, or scored questionnaire into a temporary RooQuiz preview link for review and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scorecard questions, answers, scoring rules, and embedded text are sent to RooQuiz's external preview service. <br>
Mitigation: Do not include secrets, regulated data, private personal data, or proprietary internal material unless you have permission to share it externally. <br>
Risk: The skill returns a temporary preview link rather than a permanently published form. <br>
Mitigation: Use generated links for short-lived preview and review workflows; recreate or publish the scorecard through RooQuiz when a lasting form is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-scorecard) <br>
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms) <br>
- [RooQuiz preview link host](https://quizster.app) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, json, shell commands] <br>
**Output Format:** [Markdown guidance with JSON examples, HTTP request details, and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a temporary share link from the returned public token; links expire after about one hour.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
