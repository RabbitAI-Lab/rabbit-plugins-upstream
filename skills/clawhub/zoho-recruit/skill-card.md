## Description: <br>
Zoho Recruit API integration with managed OAuth for managing candidates, job openings, interviews, applications, and recruitment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, recruiters, and recruiting operations teams use this skill to read, search, create, update, and delete Zoho Recruit records through a managed OAuth connection. It is suited for candidate, job opening, interview, application, and recruitment workflow automation when the user has a valid Maton API key and authorized Zoho Recruit connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change recruiting records in the connected Zoho Recruit account. <br>
Mitigation: Install only when Maton is trusted with that account and use the least-privileged Zoho or Maton connection available. <br>
Risk: Write or delete API calls could affect the wrong module or records. <br>
Mitigation: Require explicit user approval before create, update, or delete calls, and review the target module, record IDs, and intended effect. <br>
Risk: Requests may use the wrong Zoho Recruit account when multiple connections are available. <br>
Mitigation: Include the Maton-Connection header for the intended connection when more than one connection exists. <br>
Risk: Exposure of MATON_API_KEY could allow unauthorized use through the connected Maton account. <br>
Mitigation: Keep MATON_API_KEY secret and avoid printing, logging, or committing it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [Zoho Recruit API v2 Overview](https://www.zoho.com/recruit/developer-guide/apiv2/) <br>
- [Zoho Recruit Get Records API](https://www.zoho.com/recruit/developer-guide/apiv2/get-records.html) <br>
- [Zoho Recruit Insert Records API](https://www.zoho.com/recruit/developer-guide/apiv2/insert-records.html) <br>
- [Zoho Recruit Update Records API](https://www.zoho.com/recruit/developer-guide/apiv2/update-records.html) <br>
- [Zoho Recruit Delete Records API](https://www.zoho.com/recruit/developer-guide/apiv2/delete-records.html) <br>
- [Zoho Recruit Search Records API](https://www.zoho.com/recruit/developer-guide/apiv2/search-records.html) <br>
- [Zoho Recruit Modules API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html) <br>
- [Maton](https://maton.ai) <br>
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API paths, JSON examples, and Python or JavaScript code snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an authorized Zoho Recruit connection. Read and write behavior depends on the connected account permissions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
