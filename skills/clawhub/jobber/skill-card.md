## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Jobber business data through Maton, list and inspect records, and create or update clients, jobs, invoices, quotes, schedules, properties, requests, users, and custom fields when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on real Jobber business data, including records tied to clients, jobs, invoices, quotes, schedules, and billing.

Mitigation: Use OAuth where possible, default to read and list calls, and require explicit user approval with target resource and payload details before any data-changing operation.

Risk: A task can affect the wrong Jobber account when multiple Maton profiles or Jobber connections exist.

Mitigation: Specify the intended Maton profile and Jobber connection before making API calls, especially before writes.

Risk: Long-lived API keys or provider tokens can leak through environment variables, logs, command lines, or persisted files.

Mitigation: Prefer Maton OAuth and the CLI credential store; never print, log, persist, or pass credentials on command lines.

## Reference(s):

- [Maton homepage](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, OAuth or API-key authentication, and explicit user approval before connection creation or data-changing operations.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
