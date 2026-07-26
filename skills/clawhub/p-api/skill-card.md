## Description: <br>
Automate WhatsApp messaging, interactive content, instance and group management, catalogs, and webhooks through P-API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rafacpti23](https://clawhub.ai/user/rafacpti23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to P-API for WhatsApp automation, including sending messages, managing instances and groups, working with product catalogs, and configuring webhooks or integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to operate against a real P-API and WhatsApp environment. <br>
Mitigation: Install and use it only where that connection is intended, and require review before sending messages or changing instances. <br>
Risk: API credentials and webhook destinations may expose private message or contact data if over-scoped or misconfigured. <br>
Mitigation: Use limited API keys where possible and configure only trusted HTTPS or WSS webhook destinations. <br>
Risk: Deletion, group participant changes, and bulk messaging can affect real users or conversations. <br>
Mitigation: Require explicit approval for deletion, group management, and high-volume messaging actions, and verify recipients and content before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rafacpti23/skills/p-api) <br>
- [Official P-API Website](https://papi.api.br) <br>
- [Interactive Messages Reference](references/interactive.md) <br>
- [Groups Reference](references/groups.md) <br>
- [Catalog Reference](references/catalog.md) <br>
- [Integrations Reference](references/integrations.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; API use requires a configured P-API base URL, API key, and WhatsApp instance.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
