## Description: <br>
Accesses the Eventbrite API with managed OAuth to help agents manage events, venues, ticket classes, orders, attendees, and reference data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to retrieve Eventbrite account, organization, event, order, attendee, venue, ticket, and reference data, and to prepare approved Eventbrite create, update, publish, cancel, or delete API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Maton OAuth proxy and MATON_API_KEY to access the connected Eventbrite account. <br>
Mitigation: Install only if the user trusts Maton for the Eventbrite account, keep MATON_API_KEY secret, and use the intended Eventbrite connection. <br>
Risk: Create, update, publish, cancel, and delete operations can change Eventbrite events, venues, ticket classes, orders, or attendees. <br>
Mitigation: Before any write call, require explicit user approval that names the target resource and the intended effect. <br>
Risk: When multiple Eventbrite connections exist, requests can affect the wrong connected account. <br>
Mitigation: Use the documented Maton-Connection header when more than one active Eventbrite connection is available. <br>


## Reference(s): <br>
- [ClawHub Eventbrite Skill](https://clawhub.ai/byungkyu/skills/eventbrite) <br>
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api) <br>
- [Eventbrite API Basics](https://www.eventbrite.com/platform/docs/api-basics) <br>
- [Eventbrite API Explorer](https://www.eventbrite.com/platform/docs/api-explorer) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline HTTP paths, bash commands, Python examples, JavaScript examples, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; Eventbrite write operations require explicit user approval before execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact metadata.version is 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
