## Description: <br>
Mailchimp Marketing API integration with managed OAuth for audiences, campaigns, templates, automations, reports, and subscribers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to connect through Maton-managed OAuth and manage Mailchimp audiences, subscribers, campaigns, templates, automations, reports, and batch operations. The skill is intended for email-marketing workflows where write operations are reviewed before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Maton brokers access to the connected Mailchimp account, so the skill can expose or affect email-marketing data if used with an unintended or untrusted connection. <br>
Mitigation: Install only if you trust Maton, protect the MATON_API_KEY value, and verify the exact Mailchimp connection before making requests. <br>
Risk: Write operations can create, update, delete, send, schedule, or batch-modify Mailchimp audiences, subscribers, campaigns, templates, and automations. <br>
Mitigation: Require explicit user approval before writes and confirm the target resource, recipient count, timing, and intended effect, especially before sends, scheduling, automation starts, permanent deletion, or batch operations. <br>
Risk: Multiple linked Mailchimp accounts can cause requests to run against the wrong account if the connection is ambiguous. <br>
Mitigation: Use the Maton-Connection header when more than one Mailchimp connection exists and confirm the selected connection before sensitive reads or any write operation. <br>


## Reference(s): <br>
- [Mailchimp skill on ClawHub](https://clawhub.ai/byungkyu/skills/mailchimp) <br>
- [Mailchimp Marketing API Documentation](https://mailchimp.com/developer/marketing/) <br>
- [Mailchimp Marketing API Reference](https://mailchimp.com/developer/marketing/api/) <br>
- [Mailchimp Quick Start Guide](https://mailchimp.com/developer/marketing/guides/quick-start/) <br>
- [Mailchimp Release Notes](https://mailchimp.com/developer/release-notes/) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with HTTP endpoints, shell commands, Python and JavaScript examples, and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; supports selecting a specific Mailchimp OAuth connection with the Maton-Connection header; all write operations require explicit approval.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
