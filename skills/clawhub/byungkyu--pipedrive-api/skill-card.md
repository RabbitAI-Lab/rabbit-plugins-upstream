## Description: <br>
Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and sales operations teams use this skill to work with Pipedrive CRM records through Maton-managed OAuth, including reading and managing deals, contacts, organizations, activities, notes, pipelines, and stages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Maton-managed OAuth and a MATON_API_KEY to access Pipedrive data. <br>
Mitigation: Install only if you trust Maton to broker Pipedrive access, protect MATON_API_KEY, and scope use to the intended connected account. <br>
Risk: When multiple Pipedrive connections exist, requests could target the wrong account. <br>
Mitigation: Specify the intended connection with the Maton-Connection header before making account-specific requests. <br>
Risk: Create, update, delete, and OAuth connection changes can modify CRM data or access. <br>
Mitigation: Require clear user confirmation before write operations or connection changes, including the target resource and expected effect. <br>


## Reference(s): <br>
- [ClawHub Pipedrive Skill](https://clawhub.ai/byungkyu/skills/pipedrive-api) <br>
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1) <br>
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals) <br>
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons) <br>
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations) <br>
- [Pipedrive Activities API](https://developers.pipedrive.com/docs/api/v1/Activities) <br>
- [Pipedrive Pipelines API](https://developers.pipedrive.com/docs/api/v1/Pipelines) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with inline HTTP examples and Python or JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Pipedrive OAuth account.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
