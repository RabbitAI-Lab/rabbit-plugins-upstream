## Description:

Mailchimp Marketing API integration with managed OAuth for accessing audiences, campaigns, templates, automations, reports, and subscriber management through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mailchimp email marketing resources, subscriber lists, campaigns, templates, automations, and reports from an agent session. It is suited for read-first Mailchimp workflows and user-approved changes through managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailchimp actions can send campaigns, change subscribers, delete data, or trigger automations.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before any write or high-impact operation.

Risk: OAuth tokens, API keys, or provider-issued credentials could be exposed if printed, logged, persisted, or passed through shell arguments.

Mitigation: Use Maton OAuth and the operating system credential store where available; never print, log, persist, or pass secrets on a command line, and use raw HTTP only when the CLI cannot be installed.

Risk: Multiple Maton accounts or Mailchimp connections could route requests to the wrong account.

Mitigation: Verify authentication state and specify the intended profile or connection when multiple accounts or connections exist.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailchimp)
- [Maton Homepage](https://maton.ai)
- [Mailchimp Marketing API Documentation](https://mailchimp.com/developer/marketing/)
- [Mailchimp Marketing API Reference](https://mailchimp.com/developer/marketing/api/)
- [Mailchimp Quick Start Guide](https://mailchimp.com/developer/marketing/guides/quick-start/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default to read/list operations; confirm new connections and write operations with the user.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
