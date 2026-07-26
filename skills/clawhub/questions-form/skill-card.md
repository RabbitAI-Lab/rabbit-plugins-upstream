## Description: <br>
Present multiple clarifying questions as an interactive Telegram form using inline buttons, selectable options, and an optional free-text escape hatch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edonadei](https://clawhub.ai/user/edonadei) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to collect two or more clarifying answers in Telegram before continuing a task, such as requirements gathering, onboarding, or preference collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Collected answers may include sensitive conversation data if the form asks for credentials, financial details, or other private information. <br>
Mitigation: Use the form for ordinary clarifying questions and avoid requesting sensitive information unless it is strictly necessary and handled under the user's data policy. <br>
Risk: Interrupted sessions can leave users responding to an older form without the agent having the original form state. <br>
Mitigation: When form context is missing, tell the user the prior form cannot be completed and re-send the questions before using any answers. <br>


## Reference(s): <br>
- [Form Patterns Reference](references/form-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, configuration] <br>
**Output Format:** [Markdown guidance with JSON Telegram message payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Telegram inline-button callback data in the form:<question_id>:<value> convention.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
