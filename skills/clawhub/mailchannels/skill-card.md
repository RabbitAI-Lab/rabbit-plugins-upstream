## Description: <br>
Send email via the MailChannels Email API and ingest signed delivery-event webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ttulttul](https://clawhub.ai/user/ttulttul) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure MailChannels credentials, send transactional email, and handle delivery-event webhooks with signature verification and correlation IDs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to send real email through MailChannels. <br>
Mitigation: Require explicit approval before real sends and use a dedicated or scoped API key where possible. <br>
Risk: Delivery-event webhooks may be spoofed or misattributed if signatures and account IDs are not checked. <br>
Mitigation: Verify webhook signatures, reject stale signatures, and confirm event customer_handle values match the configured MailChannels account ID. <br>
Risk: Raw delivery events can contain operational or recipient data. <br>
Mitigation: Avoid retaining raw delivery events longer than needed and deduplicate retries before updating delivery state. <br>


## Reference(s): <br>
- [MailChannels Email API documentation](https://docs.mailchannels.net/email-api/) <br>
- [ClawHub skill page](https://clawhub.ai/ttulttul/skills/mailchannels) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MailChannels API credentials and explicit review before real email sends.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
