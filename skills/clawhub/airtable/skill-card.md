## Description: <br>
Airtable API integration with managed OAuth for reading, creating, updating, deleting, and querying Airtable bases, tables, and records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Airtable schemas and records, query data with filters, and perform approved create, update, or delete operations through a Maton-managed OAuth connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Airtable records through the connected account. <br>
Mitigation: Confirm the target base, table, records, and intended effect with the user before any write operation. <br>
Risk: Requests are brokered through Maton and depend on the permissions of the connected Airtable account. <br>
Mitigation: Install only when the user trusts Maton for Airtable access, keeps MATON_API_KEY private, and grants only the Airtable permissions needed for the task. <br>
Risk: Multiple Airtable connections can route a request to the wrong account. <br>
Mitigation: Use the Maton-Connection header when more than one connection exists and verify the selected connection before changing data. <br>


## Reference(s): <br>
- [Airtable API Overview](https://airtable.com/developers/web/api/introduction) <br>
- [Airtable List Records](https://airtable.com/developers/web/api/list-records) <br>
- [Airtable Create Records](https://airtable.com/developers/web/api/create-records) <br>
- [Airtable Update Records](https://airtable.com/developers/web/api/update-record) <br>
- [Airtable Delete Records](https://airtable.com/developers/web/api/delete-record) <br>
- [Airtable Formula Reference](https://support.airtable.com/docs/formula-field-reference) <br>
- [Maton](https://maton.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/airtable) <br>


## Skill Output: <br>
**Output Type(s):** [API calls, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with HTTP paths, Python and JavaScript examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and the intended Maton Airtable connection when multiple connections exist] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
