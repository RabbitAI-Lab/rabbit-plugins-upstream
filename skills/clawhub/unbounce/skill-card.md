## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an Unbounce account through Maton, inspect accounts, pages, domains, users, and leads, and perform confirmed landing-page or lead-management actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant Maton-mediated access to an Unbounce account.

Mitigation: Install only when that access is intended, prefer OAuth, review the account and scopes during authorization, and use least-privilege account selection.

Risk: Write, lead creation, publication-related, or deletion actions can change Unbounce data.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit confirmation of the target, payload, and intended effect before any modifying request.

Risk: Multiple Maton or Unbounce connections can route a request to the wrong account.

Mitigation: Use a specific connection when more than one account or connection exists.

Risk: API keys and provider-issued tokens can leak through command lines, logs, files, or copied output.

Mitigation: Prefer OAuth and OS credential storage; never print, log, persist, or pass credentials on a command line, and use the raw HTTP fallback only when the CLI cannot be installed.

## Reference(s):

- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/unbounce)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, API calls, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or raw HTTPS examples; read/list calls are the default and writes require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
