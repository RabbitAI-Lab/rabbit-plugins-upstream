## Description: <br>
Create a temporary, shareable RooQuiz preview for personality or outcome tests where choices vote for result types and the agent returns a browser-openable preview link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rooquiz](https://clawhub.ai/user/rooquiz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to build RooQuiz outcome-test JSON, submit it to the public RooQuiz preview API, and return a short-lived browser link for review or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quiz titles, questions, choices, outcomes, and descriptions are sent to RooQuiz's preview service. <br>
Mitigation: Do not include secrets, personal data, confidential business material, or regulated information in preview content. <br>
Risk: The skill may use the default locale if the quiz language is not set. <br>
Mitigation: Set the language explicitly when the preview audience needs a specific locale. <br>


## Reference(s): <br>
- [RooQuiz preview creation endpoint](https://preview.rooquiz.com/api/preview-forms) <br>
- [RooQuiz preview link host](https://quizster.app) <br>
- [ClawHub skill page](https://clawhub.ai/rooquiz/skills/preview-outcome) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Shell commands, API calls, Links] <br>
**Output Format:** [Markdown guidance with JSON examples, HTTP or curl snippets, and a preview URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates short-lived previews; user-provided quiz content is sent to RooQuiz's preview service.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
