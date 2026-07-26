## Description: <br>
Zoho People API integration with managed OAuth for managing employees, departments, designations, attendance, leave, and arbitrary Zoho People forms, including custom forms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, HR operators, and developers use this skill to make targeted Zoho People API requests for employee, department, designation, attendance, leave, and custom form workflows through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive HR records may be exposed through broad employee, attendance, leave, or custom form reads. <br>
Mitigation: Use the least-privileged Zoho connection available, request only specific records needed for the task, and avoid broad exports unless there is a clear business need. <br>
Risk: Create, update, or delete operations can change HR records. <br>
Mitigation: Review the target resource and intended effect with the user before approving any write operation. <br>
Risk: Requests may target the wrong Zoho People account when multiple Maton connections exist. <br>
Mitigation: Specify the intended connection with the Maton-Connection header whenever multiple Zoho People connections are available. <br>
Risk: Maton brokers access to the connected Zoho People account and requires a Maton API key. <br>
Mitigation: Install only if Maton is trusted for this account, protect MATON_API_KEY as a credential, and rotate or revoke access if it is exposed. <br>


## Reference(s): <br>
- [ClawHub Zoho People Skill Page](https://clawhub.ai/byungkyu/skills/zoho-people) <br>
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html) <br>
- [Zoho People Get Bulk Records API](https://www.zoho.com/people/api/bulk-records.html) <br>
- [Zoho People Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html) <br>
- [Zoho People Insert Record API](https://www.zoho.com/people/api/insert-records.html) <br>
- [Zoho People Update Records API](https://www.zoho.com/people/api/update-records.html) <br>
- [Zoho People Attendance Entries API](https://www.zoho.com/people/api/attendance-entries.html) <br>
- [Zoho People Add Leave API](https://www.zoho.com/people/api/add-leave.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline Python, JavaScript, HTTP, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an authorized Zoho People connection; write operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
