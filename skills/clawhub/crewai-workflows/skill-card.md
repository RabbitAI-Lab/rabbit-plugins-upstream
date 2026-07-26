## Description: <br>
Execute AI-powered crew workflows for marketing content generation, customer support handling, data analysis, and social media calendar creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rita5fr](https://clawhub.ai/user/rita5fr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, operators, and content teams can use this skill to call remote CrewAI workflows for marketing copy, support responses, business-data analysis, and 30-day social media calendars. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes a real-looking API key in published instructions. <br>
Mitigation: Treat the key as exposed, rotate it if it is real, and use environment variables or other secret-management practices instead of hardcoding or passing keys on the command line. <br>
Risk: User inputs and generated responses are sent to crew.iclautomation.me and model providers, which may expose business or customer data. <br>
Mitigation: Send only data the user is authorized to share with the remote service and review organizational data-handling requirements before use. <br>
Risk: The helper script saves full workflow responses to temporary files, which can retain sensitive outputs locally. <br>
Mitigation: Disable or modify automatic response saving when outputs may contain confidential information, and clean temporary files after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rita5fr/skills/crewai-workflows) <br>
- [CrewAI workflow service](https://crew.iclautomation.me) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions, shell command examples, and structured JSON responses from remote workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key and sends user-provided inputs to a remote CrewAI service; social media workflows may take several minutes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
