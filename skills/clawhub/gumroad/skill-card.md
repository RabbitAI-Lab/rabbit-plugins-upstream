## Description:

Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and storefront operators use this skill to connect a Gumroad account through Maton, inspect storefront data, verify licenses, and prepare product, subscriber, sales, and webhook API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned third-party CLI or SDK installation could install an unexpected Maton package version.

Mitigation: Install Maton only from official package sources and review the package source before use.

Risk: Long-lived API keys and provider-issued tokens can expose Gumroad access if printed, logged, or stored insecurely.

Mitigation: Prefer OAuth, keep credentials in the OS credential store, and never print, persist, or pass tokens on command lines.

Risk: Write, delete, license, or webhook operations can change storefront behavior or customer-facing data.

Mitigation: Start with read/list calls, identify the target connection and resource, and require explicit user approval before executing mutating API calls.

Risk: Gumroad API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and validate values before follow-up API calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton](https://maton.ai)
- [Maton Documentation](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Gumroad API Overview](https://gumroad.com/api)
- [Gumroad License Keys Help](https://help.gumroad.com/article/76-license-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON or form-encoded API payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list operations and require explicit user approval before connection creation, write, delete, or webhook changes.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
