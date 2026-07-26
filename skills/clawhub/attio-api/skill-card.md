## Description: <br>
Attio API integration with managed OAuth for creating, reading, updating, deleting, and querying CRM data including people, companies, tasks, notes, comments, lists, meetings, and call recordings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and CRM operators use this skill to work with Attio CRM records and workspace data through Maton's managed OAuth API proxy. It supports read and write workflows for objects, records, tasks, notes, comments, lists, meetings, and related CRM resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change CRM records, notes, meetings, and call recordings in the connected Attio workspace. <br>
Mitigation: Install it only for intended Attio workspaces and approve create, update, or delete actions only after checking the exact target and effect. <br>
Risk: MATON_API_KEY grants access to the Maton-managed Attio connection. <br>
Mitigation: Keep MATON_API_KEY private, provide it only through the agent environment, and rotate it if exposure is suspected. <br>
Risk: Multiple Maton connections can point requests at the wrong Attio account. <br>
Mitigation: Use the Maton-Connection header when multiple accounts exist and verify the selected connection before sensitive operations. <br>
Risk: CRM notes, meetings, and call recordings may contain sensitive business or personal data. <br>
Mitigation: Limit prompts and outputs to the minimum necessary data and review retrieved content before sharing it outside the intended workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/attio-api) <br>
- [Attio API Overview](https://docs.attio.com/rest-api/overview) <br>
- [Attio API Reference](https://docs.attio.com/rest-api/endpoint-reference) <br>
- [Records API](https://docs.attio.com/rest-api/endpoint-reference/records) <br>
- [Objects API](https://docs.attio.com/rest-api/endpoint-reference/objects) <br>
- [Tasks API](https://docs.attio.com/rest-api/endpoint-reference/tasks) <br>
- [Rate Limiting](https://docs.attio.com/rest-api/guides/rate-limiting) <br>
- [Pagination](https://docs.attio.com/rest-api/guides/pagination) <br>
- [Maton](https://maton.ai) <br>
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline Python, JavaScript, HTTP, JSON, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a valid Attio OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
