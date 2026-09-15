## Description:

Mailchimp Marketing API integration with managed OAuth for accessing audiences, campaigns, templates, automations, reports, and subscribers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help marketers and operations teams manage Mailchimp audiences, subscribers, campaigns, templates, automations, and reports through an authenticated Maton connection. It is suited for read-first email marketing workflows and approved changes such as subscriber updates, campaign scheduling, or campaign sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External CLI installation and account connection setup can expose users to package-source and authorization-flow trust decisions.

Mitigation: Install only from trusted Maton package sources, verify package source before installation, and use the managed OAuth flow for account authorization.

Risk: Raw API key use can leak a long-lived credential through logs, shell history, crash output, or child processes.

Mitigation: Prefer OAuth through the Maton CLI, use raw HTTP only when the CLI cannot be installed, never print or persist the key, and rotate it if exposed.

Risk: Mailchimp write operations, especially campaign sends, can change business data, contact records, automations, or send real email.

Mitigation: Default to read and list calls, verify target resources and payloads, and obtain explicit user approval before every POST, PUT, PATCH, DELETE, schedule, or send operation.

Risk: Hosted functions and triggers can create persistent automation that runs under the connected account and may process sensitive event or Mailchimp data.

Mitigation: Use user-authored or user-reviewed handlers, deploy with least privilege and deny outbound network access unless specifically approved, and confirm each deployment, trigger, destination, or invocation separately.

## Reference(s):

- [ClawHub Mailchimp Skill](https://clawhub.ai/byungkyu/skills/mailchimp)
- [Maton Homepage](https://maton.ai)
- [Mailchimp Marketing API Documentation](https://mailchimp.com/developer/marketing/)
- [Mailchimp Marketing API Reference](https://mailchimp.com/developer/marketing/api/)
- [Mailchimp Quick Start Guide](https://mailchimp.com/developer/marketing/guides/quick-start/)
- [Mailchimp Release Notes](https://mailchimp.com/developer/release-notes/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task guidance and executable command examples for authenticated Mailchimp API operations; responses from Mailchimp may contain personal or business data.]

## Skill Version(s):

1.2.2 (source: server release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
