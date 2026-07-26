## Description: <br>
WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and managing customer conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, and business operations teams use this skill to work with WhatsApp Business through Maton-managed OAuth, including sending messages, managing templates and media, and checking account resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send WhatsApp messages or modify templates, media, connections, and business profile data for the connected account. <br>
Mitigation: Confirm recipients, message contents, connection IDs, target resources, and destructive or mutating changes with the user before running write operations. <br>
Risk: The MATON_API_KEY grants access through Maton to WhatsApp Business account data and actions. <br>
Mitigation: Keep MATON_API_KEY private, avoid printing or storing it in shared logs, and revoke unused OAuth connections. <br>
Risk: Multiple WhatsApp Business connections can route a request to the wrong account if the target connection is ambiguous. <br>
Mitigation: Use the Maton-Connection header when multiple connections exist and verify the intended account before making API calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/whatsapp-business) <br>
- [Maton](https://maton.ai) <br>
- [WhatsApp Business API overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview) <br>
- [WhatsApp send messages guide](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages) <br>
- [WhatsApp message templates guide](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and JavaScript request examples, shell snippets, and HTTP endpoint references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations should be explicitly approved by the user.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
