## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect an agent to a Jobber account through Maton and perform read-first workflows for field-service clients, jobs, invoices, quotes, properties, requests, and team members. It can support write operations only after explicit user approval of the target resource, payload, and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate changes to Jobber records, including invoices, quotes, scheduling data, deletions, and account changes.

Mitigation: Default to read and list operations, then require explicit user approval for any write with the target resource, payload, and intended effect.

Risk: Long-lived API keys or surfaced provider credentials could be exposed through logs, files, shell history, or child processes.

Mitigation: Prefer OAuth through Maton with the narrowest available Jobber scopes, keep credentials in the approved credential store, and do not print, persist, or pass credentials on command lines.

Risk: Multiple Maton profiles or Jobber connections can make the affected account ambiguous.

Mitigation: Specify the intended profile or connection when more than one exists and confirm the account context before making changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jobber)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, valid Maton authentication, and an active Jobber connection.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
