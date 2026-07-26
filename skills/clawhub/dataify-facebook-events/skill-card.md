## Description: <br>
Submit Dataify Facebook Event Builder tasks for collecting Facebook events by event list URL, event search URL, or event URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Dataify Builder jobs that collect Facebook event data, then receive the task ID, status, and dashboard link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A saved DATAIFY_API_TOKEN may be used to create a Dataify Builder task. <br>
Mitigation: Review the selected mode, Facebook URLs, and file name before submission, and do not submit without an intentional API TOKEN. <br>
Risk: The skill creates external Dataify collection jobs that may target unintended Facebook event URLs. <br>
Mitigation: Confirm the collection mode and require URLs to start with https://www.facebook.com/ before calling the Builder endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-events) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with optional shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected mode, spider ID, task ID, status, URL parameters, file name, and dashboard URL after submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
