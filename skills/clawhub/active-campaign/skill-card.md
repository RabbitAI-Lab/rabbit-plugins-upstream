## Description:

ActiveCampaign API integration with managed OAuth for marketing automation, CRM, contacts, deals, campaigns, automations, tags, lists, users, accounts, custom fields, notes, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operators use this skill to inspect and manage ActiveCampaign contacts, deals, tags, lists, automations, campaigns, users, accounts, custom fields, notes, and webhooks through Maton-mediated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned third-party CLI or SDK installation can introduce supply-chain or version-drift risk.

Mitigation: Verify the Maton package or Homebrew tap source before installation and pin versions where the deployment process allows it.

Risk: Long-lived API keys and CRM credentials can be exposed through environment variables, command lines, logs, shell history, or persisted files.

Mitigation: Prefer OAuth and the operating system credential store; when an API key is unavoidable, keep it out of command arguments and logs, do not persist it, and rotate it if exposed.

Risk: Write, deletion, account-management, and webhook operations can modify shared CRM data, team access, or create standing egress of account event data.

Mitigation: Default to read/list calls, verify resource identifiers and account context, and require explicit user confirmation for the target, payload, destination, and intended effect before executing high-impact operations.

## Reference(s):

- [ClawHub ActiveCampaign Skill](https://clawhub.ai/byungkyu/skills/active-campaign)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ActiveCampaign API Overview](https://developers.activecampaign.com/reference/overview)
- [ActiveCampaign Developer Portal](https://developers.activecampaign.com/)
- [ActiveCampaign API Base URL](https://developers.activecampaign.com/reference/url)
- [ActiveCampaign Contacts API](https://developers.activecampaign.com/reference/list-all-contacts)
- [ActiveCampaign Tags API](https://developers.activecampaign.com/reference/contact-tags)
- [ActiveCampaign Deals API](https://developers.activecampaign.com/reference/list-all-deals)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for read and write ActiveCampaign API workflows; write, deletion, account-management, connection, and webhook operations require explicit user approval.]

## Skill Version(s):

1.2.1 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
