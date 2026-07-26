## Description: <br>
Basecamp API integration with managed OAuth for managing projects, to-dos, messages, schedules, documents, and team collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Basecamp 4 through Maton's managed OAuth gateway for project, to-do, message, schedule, document, and team collaboration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on Maton to mediate access to a connected Basecamp account. <br>
Mitigation: Install only when Maton is trusted for the account, review the connected Basecamp permissions, and keep MATON_API_KEY private. <br>
Risk: Write operations can create, update, archive, trash, or post Basecamp content. <br>
Mitigation: Require explicit user confirmation before each write operation, including the target resource and intended effect. <br>
Risk: Multiple Basecamp connections can cause requests to affect the wrong account. <br>
Mitigation: Use the Maton-Connection header when more than one Basecamp connection exists. <br>


## Reference(s): <br>
- [ClawHub Basecamp Skill](https://clawhub.ai/byungkyu/skills/basecamp) <br>
- [Basecamp 4 API Documentation](https://github.com/basecamp/bc3-api) <br>
- [Basecamp Authentication Guide](https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md) <br>
- [Basecamp API Endpoint Reference](https://github.com/basecamp/bc3-api#endpoints) <br>
- [Related Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>
- [Maton API Key Settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP endpoint, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY, network access, and a Basecamp OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
