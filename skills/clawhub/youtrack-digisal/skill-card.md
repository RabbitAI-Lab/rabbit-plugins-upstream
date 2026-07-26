## Description: <br>
Interact with YouTrack through its REST API to read projects and issues, create tasks, generate invoices from time tracking data, and manage knowledge base articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[digisal](https://clawhub.ai/user/digisal) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project teams use this skill to work with YouTrack projects, issues, time tracking data, generated client invoices, and knowledge base articles from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTrack API tokens and project data are sensitive. <br>
Mitigation: Use a scoped API token, prefer the YOUTRACK_TOKEN environment variable over command-line token arguments, and verify the YouTrack URL before running commands. <br>
Risk: Generated invoices may contain incorrect billing details or internal issue information. <br>
Mitigation: Manually review client scope, dates, rates, rounding, names, and issue details before sharing invoice output. <br>


## Reference(s): <br>
- [YouTrack API References](REFERENCES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Python and shell command examples; generated invoices are plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a YouTrack instance URL and API token; invoice output depends on selected project, date range, month label, and hourly rate.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
