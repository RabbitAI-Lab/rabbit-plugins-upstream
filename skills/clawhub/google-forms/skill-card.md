## Description: <br>
Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect agents to Google Forms through Maton-managed OAuth, then retrieve form data or create and update forms with user-approved API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Google Forms content and responses through a connected Google account. <br>
Mitigation: Install only when Maton is trusted to broker the account connection, keep MATON_API_KEY private, and verify the selected connection when multiple accounts are available. <br>
Risk: Create, update, or delete operations can change Google Forms resources. <br>
Mitigation: Approve write operations only after checking the exact form ID, target resource, and intended change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-forms) <br>
- [Google Forms API Overview](https://developers.google.com/workspace/forms/api/reference/rest) <br>
- [Get Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/get) <br>
- [Create Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create) <br>
- [Batch Update Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate) <br>
- [List Responses](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with Python, JavaScript, shell command, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a valid Maton-managed Google Forms OAuth connection.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
