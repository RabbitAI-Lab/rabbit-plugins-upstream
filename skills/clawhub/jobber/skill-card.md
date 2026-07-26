## Description: <br>
Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and field service operators use this skill to access Jobber through Maton's managed OAuth gateway, inspect account data, and create or update operational records such as clients, jobs, invoices, quotes, properties, and team members. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Jobber business data and perform changes to clients, jobs, invoices, quotes, schedules, and account records through Maton's OAuth gateway. <br>
Mitigation: Install only if you trust Maton to broker Jobber access, and require explicit user approval before any create, update, or delete operation. <br>
Risk: Requests may target the wrong Jobber account when multiple connections are linked. <br>
Mitigation: Verify the selected Jobber connection before use and include the intended connection identifier when multiple accounts are available. <br>


## Reference(s): <br>
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/) <br>
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/) <br>
- [Jobber skill page](https://clawhub.ai/byungkyu/skills/jobber) <br>
- [Related Maton API gateway skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with Python, JavaScript, GraphQL, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Jobber OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
