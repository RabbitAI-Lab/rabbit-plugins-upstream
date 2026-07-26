## Description: <br>
HubSpot CRM and CMS API integration for contacts, companies, deals, owners, and content management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwall1](https://clawhub.ai/user/kwall1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and business operations teams use this skill to generate HubSpot REST API commands for CRM and CMS tasks such as reading records, creating contacts or deals, assigning owners, managing associations, and inspecting content assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A HubSpot private app token can allow the agent to read or change CRM and CMS data. <br>
Mitigation: Use a least-privilege token and confirm the intended HubSpot account, scopes, and target records before running commands. <br>
Risk: Create, update, owner assignment, and association commands can modify production HubSpot records. <br>
Mitigation: Prefer sandbox or test records during setup, and explicitly review write requests before executing them against production data. <br>


## Reference(s): <br>
- [HubSpot API base endpoint](https://api.hubapi.com) <br>
- [ClawHub skill page](https://clawhub.ai/kwall1/skills/hubspot) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash and PowerShell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and HUBSPOT_ACCESS_TOKEN; HubSpot API responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
