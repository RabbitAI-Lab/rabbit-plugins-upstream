## Description: <br>
Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book searches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to read, create, update, and delete Google Contacts and contact groups through Maton's managed OAuth proxy. It is suited for address book lookup, contact maintenance, group management, and Google People API troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete contacts and contact groups in a connected Google account. <br>
Mitigation: Confirm the active Google connection, target resource, and intended effect before any write operation. <br>
Risk: Deleting a contact group with deleteContacts=true can also delete member contacts. <br>
Mitigation: Use deleteContacts=false unless the user explicitly approves deleting both the group and its member contacts. <br>
Risk: The integration depends on Maton as the OAuth proxy for Google Contacts. <br>
Mitigation: Install and use the skill only when the user trusts Maton to broker the Google Contacts connection. <br>


## Reference(s): <br>
- [Google People API Overview](https://developers.google.com/people/api/rest) <br>
- [People Resource](https://developers.google.com/people/api/rest/v1/people) <br>
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups) <br>
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with API endpoints, JSON examples, and Python or JavaScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; API responses are JSON.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
