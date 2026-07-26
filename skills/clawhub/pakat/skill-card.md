## Description: <br>
Interact with Pakat email marketing API (new.pakat.net) - REQUIRES PAKAT_API_KEY environment variable. Use when the user wants to manage email lists, subscribers, campaigns, templates, transactional emails, segments, or check campaign stats and delivery logs via the Pakat platform. Triggers on mentions of Pakat, email campaigns, mailing lists, subscriber management, or transactional email sending through Pakat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hadifarnoud](https://clawhub.ai/user/hadifarnoud) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to operate a Pakat email-marketing account through the REST API, including mailing lists, subscribers, campaigns, templates, transactional email, segments, stats, and delivery logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send or schedule marketing and transactional emails, which may create reputational, compliance, or customer-impacting consequences. <br>
Mitigation: Require explicit user confirmation before sending or scheduling emails, and verify sender identity, recipient lists, subject, body, and scheduled time. <br>
Risk: The skill can delete or change lists, subscribers, templates, campaigns, and customer account resources. <br>
Mitigation: Use the least-privileged Pakat API key available and require confirmation before destructive or account-changing requests. <br>
Risk: Pasting PAKAT_API_KEY into chat or logs can expose control of the Pakat account. <br>
Mitigation: Configure PAKAT_API_KEY through a secure environment or secret store. <br>
Risk: HTML email content that is encoded unsafely in shell commands can introduce command-injection risk. <br>
Mitigation: Use heredocs or temporary files for base64 encoding and avoid echoing unsanitized content into shell commands. <br>


## Reference(s): <br>
- [Pakat API Reference](references/api_reference.md) <br>
- [Pakat OpenAPI Specification](references/openapi.json) <br>
- [Pakat Website](https://pakat.net) <br>
- [Pakat API Keys](https://new.pakat.net/customer/api-keys/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and PAKAT_API_KEY; API responses are returned by the Pakat service.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
