## Description: <br>
Send transactional and marketing emails via UniOne Email API, manage email templates, validate email addresses, check delivery statistics, manage suppression lists, configure webhooks, and handle domain settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[selzy-openclaw](https://clawhub.ai/user/selzy-openclaw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to let an agent operate UniOne email workflows, including sending messages, validating recipients, managing templates, configuring delivery tracking, and reviewing account delivery data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through sensitive email-account actions such as sending messages, changing webhooks, deleting resources, changing projects, and exporting event data. <br>
Mitigation: Require manual review and approval before sends, webhook changes, deletions, project changes, or event exports. <br>
Risk: UniOne API access can expose or affect recipient activity data, including webhook callbacks, tracking data, event dumps, and download URLs. <br>
Mitigation: Treat those artifacts as sensitive data and use a least-privileged UniOne API key when available. <br>
Risk: Retries for email sends can duplicate messages if the request is not idempotent. <br>
Mitigation: Use a unique idempotency key for each logical send operation and reuse that key when retrying the same send. <br>
Risk: Email delivery fails when the sender domain is not verified. <br>
Mitigation: Verify the sending domain and DKIM records before attempting production sends. <br>


## Reference(s): <br>
- [UniOne API Documentation](https://docs.unione.io/en/web-api-ref) <br>
- [UniOne Getting Started Guide](https://docs.unione.io/en/) <br>
- [UniOne Template Engines](https://docs.unione.io/en/web-api#section-template-engines) <br>
- [UniOne Website](https://unione.io/en/) <br>
- [ClawHub Skill Page](https://clawhub.ai/selzy-openclaw/skills/unione) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON, curl, and language-specific code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for UniOne API requests and account operations; the skill itself is documentation-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
